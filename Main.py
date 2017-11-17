#!/usr/bin/python

from Util.JoomlaUtil import JoomlaUtil
from Util.WordpressUtil import WordpressUtil

print("JOOMLA")

db_joomla_host = input("Joomla database host:")
db_joomla_name = input("Joomla database name:")
db_joomla_user = input("Joomla database user:")
db_joomla_pass = input("Joomla database password:")

print("WORDPRESS")

db_wp_host = input("Wordpress database host:")
db_wp_name = input("Wordpress database name:")
db_wp_user = input("Wordpress database user:")
db_wp_pass = input("Wordpress database password:")
db_table_prefix = input("Wordpress database prefix:")
site_url = input("Wordpress site url:")
site_username = input("Wordpress site username:")
site_password = input("Wordpress site password:")

joomla_config = {
    "db_joomla_host": db_joomla_host,
    "db_joomla_name": db_joomla_name,
    "db_joomla_user": db_joomla_user,
    "db_joomla_pass": db_joomla_pass,
}

wp_config = {
    "db_wp_host": db_wp_host,
    "db_wp_name": db_wp_name,
    "db_wp_user": db_wp_user,
    "db_wp_pass": db_wp_pass,
    "db_table_prefix": db_table_prefix,

    "site_url": site_url,
    "site_password": site_password,
    "site_username": site_username,
}

joomla_util = JoomlaUtil(config=joomla_config)

# Funcoes do Joomla        ##
list_of_categories_joomla = joomla_util.import_categories_k2()
list_of_posts_joomla = joomla_util.import_posts_k2()

# Funcoes do Wordpress     ##
wp_util = WordpressUtil(config=wp_config)

wp_util.remove_all_posts()
wp_util.remove_all_categories()

ref_categories = wp_util.insert_categories(list_of_categories_joomla)
wp_util.insert_posts(list_of_posts_joomla, ref_categories)
