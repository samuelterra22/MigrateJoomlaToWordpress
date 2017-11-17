#  http://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html
# sudo python3.5 -m pip install mysqlclient


from xmlrpc import client

import MySQLdb
from numpy.matlib import rand, random
from wordpress_xmlrpc import xmlrpc_client, WordPressTerm
from wordpress_xmlrpc.methods import media, taxonomies
from wordpress_xmlrpc import Client, WordPressPost
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
        db = self.get_connection()

        table = str(self._db_table_prefix) + "term_taxonomy"

        cur = db.cursor()
        cur.execute("DELETE FROM " + table + " WHERE taxonomy = 'post_tag'")
        db.commit()
        result = cur.fetchall()

        db.close()

        return result

    def post_thumbnail(self, client):
        # set to the path to your file
        # filename = 'imagens/' + md5('Image' + id_post_joomla) + '.jpg'
        filename = 'b414e2ba4719c9b4ceec2e3c09e2491b.jpg'

        # prepare metadata
        data = {
            'name': 'picture.jpg',
            'type': 'image/jpeg',  # mimetype
        }

        # read the binary file and let the XMLRPC library encode it into base64
        with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

        response = client.call(media.UploadFile(data))
        # response == {
        #       'id': 6,
        #       'file': 'picture.jpg'
        #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
        #       'type': 'image/jpeg',
        # }
        return response

    def post_category(self, category_joomla, ref_cat):
        client = Client(str(self._site_url) + '/xmlrpc.php', self._site_username, self._site_password)

        idx = random.randint(0, 80)

        cat = WordPressTerm()
        cat.taxonomy = 'category'

        if category_joomla.get_parent() != 0:
            # id da categoria pai
            cat.parent = ref_cat.get(category_joomla.get_parent())
            parent = str(cat.parent)

        cat.name = category_joomla.get_name()
        cat.slug = str(idx) + str(cat.name)
        cat.id = client.call(taxonomies.NewTerm(cat))

        print(cat.slug)

        return cat.id

    def post_categories(self, categories_joomla):

        # sort by parent
        sorted_categories_joomla = sorted(categories_joomla, key=lambda category: category.get_id())

        ref_categories = {}

        for category_joomla in sorted_categories_joomla:
            new_id = self.post_category(category_joomla, ref_categories)
            old_id = category_joomla.get_parent()
            ref_categories.update({old_id: new_id})

    def post_to_wp(self, wp_post):
        client = Client(str(self._site_url) + '/xmlrpc.php', self._site_username, self._site_password)
        post = WordPressPost()
        post.title = 'My new title'
        post.content = 'This is the body of my new post.'
        post.thumbnail = self.post_thumbnail(client)['id']
        post.post_status = "publish"
        post.terms_names = {
            # 'post_tag': ['test', 'firstpost'],
            'category': ['Introductions', 'Tests']
        }
        client.call(NewPost(post))

        return post
