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
# print(len(joomla_util.import_categories_k2()))
# print(joomla_util.remove_all_posts())


wp_config = {
    "db_wp_host": "localhost",
    "db_wp_user": "root",
    "db_wp_pass": "",
    "db_wp_name": "corrego_teste_wp",
    "db_table_prefix": "wp_"
}

wp_util = WordpressUtil(config=wp_config)

# print(wp_util.remove_all_posts())
# print(wp_util.remove_all_categories())
