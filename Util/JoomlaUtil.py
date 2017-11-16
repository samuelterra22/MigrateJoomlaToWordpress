import MySQLdb

from Model.JoomlaCategoryK2 import JoomlaCategoryK2
from Model.JoomlaPostK2 import JoomlaPostK2


class JoomlaUtil(object):

    def __init__(self, config):
        self._db_joomla_host = config["db_joomla_host"]
        self._db_joomla_user = config["db_joomla_user"]
        self._db_joomla_pass = config["db_joomla_pass"]
        self._db_joomla_name = config["db_joomla_name"]

    def get_connection(self):
        return MySQLdb.connect(
            host=self._db_joomla_host,  # your host, usually localhost
            user=self._db_joomla_user,  # your username
            passwd=self._db_joomla_pass,  # your password
            db=self._db_joomla_name  # name of the data base
        )

    def import_posts_k2(self):
        
        db = self.get_connection()

        cur = db.cursor()
        cur.execute("SELECT * FROM npols_k2_items")

        posts = []

        for row in cur.fetchall():
            data = {
                "id": row[0],
                "title": row[1],
                "alias": row[2],
                "catid": row[3],
                "published": row[4],
                "introtext": row[5],
                "fulltext": row[6],
                "video": row[7],
                "gallery": row[8],
                "extra_fields": row[9],
                "extra_fields_search": row[10],
                "created": row[11],
                "created_by": row[12],
                "created_by_alias": row[13],
                "checked_out": row[14],
                "checked_out_time": row[15],
                "modified": row[16],
                "modified_by": row[17],
                "publish_up": row[18],
                "publish_down": row[19],
                "trash": row[20],
                "access": row[21],
                "ordering": row[22],
                "featured": row[23],
                "featured_ordering": row[24],
                "image_caption": row[25],
                "image_credits": row[26],
                "video_caption": row[27],
                "video_credits": row[28],
                "hits": row[29],
                "params": row[30],
                "metadesc": row[31],
                "metadata": row[32],
                "metakey": row[33],
                "plugins": row[34],
                "language": row[35]
            }

            post_k2 = JoomlaPostK2(data=data)

            posts.append(post_k2)

        db.close()

        return posts

    def import_categories_k2(self):
        db = self.get_connection()

        cur = db.cursor()
        cur.execute("SELECT * FROM npols_k2_categories")

        categories = []

        for row in cur.fetchall():
            data = {
                "id": row[0],
                "name": row[1],
                "alias": row[2],
                "description": row[3],
                "parent": row[4],
                "extraFieldsGroup": row[5],
                "published": row[6],
                "access": row[7],
                "ordering": row[8],
                "image": row[9],
                "params": row[10],
                "trash": row[11],
                "plugins": row[12],
                "language": row[13],
            }

            category_k2 = JoomlaCategoryK2(data=data)

            categories.append(category_k2)

        db.close()

        return categories

    def remove_all_posts(self):
        db = self.get_connection()

        cur = db.cursor()
        cur.execute("DELETE FROM npols_k2_items")

        result = cur.fetchall()

        db.close()

        return result
