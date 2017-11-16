#!/usr/bin/python

from Util.JoomlaUtil import JoomlaUtil
from Util.WordpressUtil import WordpressUtil

joomla_config = {
    "db_joomla_host": "localhost",
    "db_joomla_user": "root",
    "db_joomla_pass": "",
    "db_joomla_name": "corrego_teste",
}

joomla_util = JoomlaUtil(config=joomla_config)

# print(len(joomla_util.import_posts_k2()))
# print(joomla_util.remove_all_posts())
# categories = joomla_util.import_categories_k2()
#
#
# sorted_categories = sorted(categories, key=lambda category: category.get_parent())   # sort by parent
#
#
# # print(sorted_categories)
# for cat in sorted_categories:
#     print(cat.get_id())





wp_config = {
    "db_wp_host": "localhost",
    "db_wp_user": "root",
    "db_wp_pass": "",
    "db_wp_name": "corrego_teste_wp",
    "db_table_prefix": "wp_",

    "site_url": "http://localhost/corrego_teste",
    "site_password": "*0109lr*",
    "site_username": "suporte",

    # "site_url": "http://local.corrego",
    # "site_password": "#cs0117sw#"
}

wp_util = WordpressUtil(config=wp_config)

# wp_util.remove_all_posts()
# wp_util.remove_all_categories()
# wp_util.post_to_wp(None)
wp_util.post_category(None)
