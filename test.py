def entry():
    config = {}

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

    return config.update({
        "db_joomla_host": db_joomla_host,
        "db_joomla_name": db_joomla_name,
        "db_joomla_user": db_joomla_user,
        "db_joomla_pass": db_joomla_pass,
        "db_wp_host": db_wp_host,
        "db_wp_name": db_wp_name,
        "db_wp_user": db_wp_user,
        "db_wp_pass": db_wp_pass,
        "db_table_prefix": db_table_prefix,
        "site_url": site_url,
        "site_username": site_username,
        "site_password": site_password
    })


entries = entry()