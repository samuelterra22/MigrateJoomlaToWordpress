#  http://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.users import GetUserInfo

import MySQLdb


class WordpressUtil(object):
    def __init__(self, config):
        self._db_wp_host = config["db_wp_host"]
        self._db_wp_user = config["db_wp_user"]
        self._db_wp_pass = config["db_wp_pass"]
        self._db_wp_name = config["db_wp_name"]

        self._db_table_prefix = config["db_table_prefix"]

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

        table = str(self._db_table_prefix) + "term_taxonomy"

        cur = db.cursor()
        cur.execute("DELETE FROM " + table + " WHERE term_taxonomy_id != 1 AND taxonomy = 'category'")
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

# client = Client('http://localhost/corrego_teste/xmlrpc.php', 'suporte', '*0109lr*')
#
# # set to the path to your file
# # filename = 'imagens/' + md5('Image' + id_post_joomla) + '.jpg'
# filename = 'b414e2ba4719c9b4ceec2e3c09e2491b.jpg'
#
# # prepare metadata
# data = {
#     'name': 'picture.jpg',
#     'type': 'image/jpeg',  # mimetype
# }
#
# # read the binary file and let the XMLRPC library encode it into base64
# with open(filename, 'rb') as img:
#     data['bits'] = xmlrpc_client.Binary(img.read())
#
# response = client.call(media.UploadFile(data))
# # response == {
# #       'id': 6,
# #       'file': 'picture.jpg'
# #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
# #       'type': 'image/jpeg',
# # }
# attachment_id = response['id']
#
# post = WordPressPost()
# post.title = 'My new title'
# post.content = 'This is the body of my new post.'
# post.thumbnail = attachment_id
# post.terms_names = {
#     'post_tag': ['test', 'firstpost'],
#     'category': ['Introductions', 'Tests']
# }
# client.call(NewPost(post))
