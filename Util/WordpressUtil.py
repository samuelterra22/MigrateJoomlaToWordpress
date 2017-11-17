import hashlib
from io import BytesIO

import MySQLdb
import progressbar
import requests
from numpy.matlib import random
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc import xmlrpc_client, WordPressTerm
from wordpress_xmlrpc.methods import media, taxonomies
from wordpress_xmlrpc.methods.posts import NewPost


class WordpressUtil(object):
    def __init__(self, config):
        self._db_wp_host = config["db_wp_host"]
        self._db_wp_user = config["db_wp_user"]
        self._db_wp_pass = config["db_wp_pass"]
        self._db_wp_name = config["db_wp_name"]

        self._db_table_prefix = config["db_table_prefix"]
        self._site_url = config["site_url"]
        self._site_username = config["site_username"]
        self._site_password = config["site_password"]

    def get_connection(self):
        return MySQLdb.connect(
            host=self._db_wp_host,  # your host, usually localhost
            user=self._db_wp_user,  # your username
            passwd=self._db_wp_pass,  # your password
            db=self._db_wp_name  # name of the data base
        )

    def remove_all_posts(self):
        print("Apagando registros de posts...")

        db = self.get_connection()

        table = str(self._db_table_prefix) + "posts"

        cur = db.cursor()
        query = "DELETE FROM " + str(table)
        cur.execute(query)
        db.commit()
        result = cur.fetchall()

        db.close()

        return result

    def remove_all_categories(self):
        print("Apagando registros de categorias...")

        db = self.get_connection()
        cur = db.cursor()

        table = str(self._db_table_prefix) + "term_taxonomy"
        cur.execute("DELETE FROM " + table + " WHERE term_taxonomy_id != 1 AND taxonomy = 'category'")
        db.commit()

        table = str(self._db_table_prefix) + "terms"
        cur.execute("DELETE FROM " + table + " WHERE term_id != 1 AND slug != 'sem-categoria'")
        db.commit()

        result = cur.fetchall()

        db.close()

        return result

    def remove_all_post_tags(self):
        print("Apagando registros de tags de posts...")

        db = self.get_connection()

        table = str(self._db_table_prefix) + "term_taxonomy"

        cur = db.cursor()
        cur.execute("DELETE FROM " + table + " WHERE taxonomy = 'post_tag'")
        db.commit()
        result = cur.fetchall()

        db.close()

        return result

    def get_client(self):
        return Client(str(self._site_url) + '/xmlrpc.php', self._site_username, self._site_password)

    def get_name_thumbnail(self, post_id):
        m = hashlib.md5()
        img_name = "Image" + str(post_id)
        m.update(img_name.encode('utf-8'))
        return m.hexdigest()

    def post_thumbnail(self, post_id):

        response = requests.get(
            "http://corregofundo.mg.gov.br/media/k2/items/src/" + str(self.get_name_thumbnail(post_id)) + ".jpg")

        img = BytesIO(response.content)

        client = self.get_client()

        # prepare metadata
        data = {
            'name': 'picture.jpg',
            'type': 'image/jpeg',
            'bits': xmlrpc_client.Binary(img.read())
        }

        response = client.call(media.UploadFile(data))

        return response

    def insert_category(self, category_joomla, ref_cat):
        client = self.get_client()

        idx = random.randint(0, 80)

        cat = WordPressTerm()
        cat.taxonomy = 'category'

        if category_joomla.get_parent() != 0:
            # id da categoria pai
            cat.parent = ref_cat.get(category_joomla.get_parent())

        cat.name = category_joomla.get_name()
        cat.slug = str(idx) + str(cat.name)
        cat.id = client.call(taxonomies.NewTerm(cat))

        # print(cat.slug)

        return cat.id

    def insert_categories(self, categories_joomla):

        # se nao estiver na lixeira
        categories_joomla = [category for category in categories_joomla if category.get_trash() != 1]

        num_categories = len(categories_joomla)

        print("----------------------------------------------")
        print("Inserindo categorias no site em Wordpress...")
        print("Total de categorias:\t" + str(num_categories) + "\n")

        ref_categories = {}

        bar = progressbar.ProgressBar()
        # Para todas as categorias do joomla
        for category_joomla in bar(categories_joomla):
            new_id = self.insert_category(category_joomla, ref_categories)
            old_id = category_joomla.get_id()
            ref_categories.update({old_id: new_id})

        return ref_categories

    def insert_post(self, joomla_post, category_id):

        client = self.get_client()
        post = WordPressPost()
        post.title = joomla_post.get_title()

        text_to_replace = joomla_post.get_introtext()

        post.content = str(text_to_replace).replace("href=\"images/", "href=\"/images/")

        post.date = joomla_post.get_created()

        post.thumbnail = self.post_thumbnail(joomla_post.get_id())['id']

        post.post_status = "publish"

        category = client.call(taxonomies.GetTerm('category', category_id))

        post.terms.append(category)

        client.call(NewPost(post))

        return post

    def insert_posts(self, posts_joomla, ref_cat):

        # se nao estiver na lixeira
        posts_joomla = [post for post in posts_joomla if post.get_trash() != 1]

        num_posts = len(posts_joomla)
        print("----------------------------------------------")
        print("Inserindo posts no site em Wordpress...")
        print("Total de posts:\t" + str(num_posts) + "\n")

        bar = progressbar.ProgressBar()
        # Para todas os posts do joomla
        for post_joomla in bar(posts_joomla):
            # print(str(round((i / num_posts) * 100, 1)) + "% concuido.")

            # if post_joomla.get_trash() != 1:
            self.insert_post(post_joomla, ref_cat.get(post_joomla.get_catid()))

        print("----------------------------------------------")
        # return ref_categories

    def fix_links(self):
        pass
