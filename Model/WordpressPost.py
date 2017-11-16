class WordpressPost(object):
    def __init__(self, data):
        self._ID = data['ID']
        self._post_author = data['post_author']
        self._post_date = data['post_date']
        self._post_date_gmt = data['post_date_gmt']
        self._post_content = data['post_content']
        self._post_title = data['post_title']
        self._post_excerpt = data['post_excerpt']
        self._post_status = data['post_status']
        self._comment_status = data['comment_status']
        self._ping_status = data['ping_status']
        self._post_password = data['post_password']
        self._post_name = data['post_name']
        self._to_ping = data['to_ping']
        self._pinged = data['pinged']
        self._post_modified = data['post_modified']
        self._post_modified_gmt = data['post_modified_gmt']
        self._post_content_filtered = data['post_content_filtered']
        self._post_parent = data['post_parent']
        self._guid = data['guid']
        self._menu_order = data['menu_order']
        self._post_type = data['post_type']
        self._post_mime_type = data['post_mime_type']
        self._comment_count = data['comment_count']

    # gets

    def get_ID(self):
        return self._ID

    def get_post_author(self):
        return self._post_author

    def get_post_date(self):
        return self._post_date

    def get_post_date_gmt(self):
        return self._post_date_gmt

    def get_post_content(self):
        return self._post_content

    def get_post_title(self):
        return self._post_title

    def get_post_excerpt(self):
        return self._post_excerpt

    def get_post_status(self):
        return self._post_status

    def get_comment_status(self):
        return self._comment_status

    def get_ping_status(self):
        return self._ping_status

    def get_post_password(self):
        return self._post_password

    def get_post_name(self):
        return self._post_name

    def get_to_ping(self):
        return self._to_ping

    def get_pinged(self):
        return self._pinged

    def get_post_modified(self):
        return self._post_modified

    def get_post_modified_gmt(self):
        return self._post_modified_gmt

    def get_post_content_filtered(self):
        return self._post_content_filtered

    def get_post_parent(self):
        return self._post_parent

    def get_guid(self):
        return self._guid

    def get_menu_order(self):
        return self._menu_order

    def get_post_type(self):
        return self._post_type

    def get_post_mime_type(self):
        return self._post_mime_type

    def get_comment_count(self):
        return self._comment_count

    # sets

    def set_ID(self, ID):
        self._ID = ID

    def set_post_author(self, post_author):
        self._post_author = post_author

    def set_post_date(self, post_date):
        self._post_date = post_date

    def set_post_date_gmt(self, post_date_gmt):
        self._post_date_gmt = post_date_gmt

    def set_post_content(self, post_content):
        self._post_content = post_content

    def set_post_title(self, post_title):
        self._post_title = post_title

    def set_post_excerpt(self, post_excerpt):
        self._post_excerpt = post_excerpt

    def set_post_status(self, post_status):
        self._post_status = post_status

    def set_comment_status(self, comment_status):
        self._comment_status = comment_status

    def set_ping_status(self, comment_status):
        self._comment_status = comment_status

    def set_post_password(self, post_password):
        self._post_password = post_password

    def set_post_name(self, post_name):
        self._post_name = post_name

    def set_to_ping(self, to_ping):
        self._to_ping = to_ping

    def set_pinged(self, pinged):
        self._pinged = pinged

    def set_post_modified(self, post_modified):
        self._post_modified = post_modified

    def set_post_modified_gmt(self, post_modified_gmt):
        self._post_modified_gmt = post_modified_gmt

    def set_post_content_filtered(self, post_content_filtered):
        self._post_content_filtered = post_content_filtered

    def set_post_parent(self, post_parent):
        self._post_parent = post_parent

    def set_guid(self, guid):
        self._guid = guid

    def set_menu_order(self, menu_order):
        self._menu_order = menu_order

    def set_post_type(self, post_type):
        self._post_type = post_type

    def set_post_mime_type(self, post_mime_type):
        self._post_mime_type = post_mime_type

    def set_comment_count(self, comment_count):
        self._comment_count = comment_count


