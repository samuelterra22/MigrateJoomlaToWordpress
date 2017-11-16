class JoomlaPostK2(object):
    
    def __init__(self, data):

        self._id = data['id']
        self._title = data['title']
        self._alias = data['alias']
        self._catid = data['catid']
        self._published = data['published']
        self._introtext = data['introtext']
        self._fulltext = data['fulltext']
        self._video = data['video']
        self._gallery = data['gallery']
        self._extra_fields = data['extra_fields']
        self._extra_fields_search = data['extra_fields_search']
        self._created = data['created']
        self._created_by = data['created_by']
        self._created_by_alias = data['created_by_alias']
        self._checked_out = data['checked_out']
        self._checked_out_time = data['checked_out_time']
        self._modified = data['modified']
        self._modified_by = data['modified_by']
        self._publish_up = data['publish_up']
        self._publish_down = data['publish_down']
        self._trash = data['trash']
        self._access = data['access']
        self._ordering = data['ordering']
        self._featured = data['featured']
        self._featured_ordering = data['featured_ordering']
        self._image_caption = data['image_caption']
        self._image_credits = data['image_credits']
        self._video_caption = data['video_caption']
        self._video_credits = data['video_credits']
        self._hits = data['hits']
        self._params = data['params']
        self._metadesc = data['metadesc']
        self._metadata = data['metadata']
        self._metakey = data['metakey']
        self._plugins = data['plugins']
        self._language = data['language']

    # gets #

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_alias(self):
        return self._alias

    def get_catid(self):
        return self._catid

    def get_published(self):
        return self._published

    def get_introtext(self):
        return self._introtext

    def get_fulltext(self):
        return self._fulltext

    def get_video(self):
        return self._video

    def get_gallery(self):
        return self._gallery

    def get_extra_fields(self):
        return self._extra_fields

    def get_extra_fields_search(self):
        return self._extra_fields_search

    def get_created(self):
        return self._created

    def get_created_by(self):
        return self._created_by

    def get_created_by_alias(self):
        return self._created_by_alias

    def get_checked_out(self):
        return self._checked_out

    def get_checked_out_time(self):
        return self._checked_out_time

    def get_modified(self):
        return self._modified

    def get_modified_by(self):
        return self._modified_by

    def get_publish_up(self):
        return self._publish_up

    def get_publish_down(self):
        return self._publish_down

    def get_trash(self):
        return self._trash

    def get_access(self):
        return self._access

    def get_ordering(self):
        return self._ordering

    def get_featured(self):
        return self._featured

    def get_featured_ordering(self):
        return self._featured_ordering

    def get_image_caption(self):
        return self._image_caption

    def get_image_credits(self):
        return self._image_credits

    def get_video_caption(self):
        return self._video_caption

    def get_video_credits(self):
        return self._video_credits

    def get_hits(self):
        return self._hits

    def get_params(self):
        return self._params

    def get_metadesc(self):
        return self._metadesc

    def get_metadata(self):
        return self._metadata

    def get_metakey(self):
        return self._metakey

    def get_plugins(self):
        return self._plugins

    def get_language(self):
        return self._language

        # sets #

    def set_id(self, id):
        self._id = id

    def set_title(self, title):
        self._title = title

    def set_alias(self, alias):
        self._alias = alias

    def set_catid(self, catid):
        self._catid = catid

    def set_published(self, published):
        self._published = published

    def set_introtext(self, introtext):
        self._introtext = introtext

    def set_fulltext(self, fulltext):
        self._fulltext = fulltext

    def set_video(self, video):
        self._video = video

    def set_gallery(self, gallery):
        self._gallery = gallery

    def set_extra_fields(self, extra_fields):
        self._extra_fields = extra_fields

    def set_extra_fields_search(self, extra_fields_search):
        self._extra_fields_search = extra_fields_search

    def set_created(self, created):
        self._created = created

    def set_created_by(self, created_by):
        self._created_by = created_by

    def set_created_by_alias(self, created_by_alias):
        self._created_by_alias = created_by_alias

    def set_checked_out(self, checked_out):
        self._checked_out = checked_out

    def set_checked_out_time(self, checked_out_time):
        self._checked_out_time = checked_out_time

    def set_modified(self, modified):
        self._modified = modified

    def set_modified_by(self, modified_by):
        self._modified_by = modified_by

    def set_publish_up(self, publish_up):
        self._publish_up = publish_up

    def set_publish_down(self, publish_down):
        self._publish_down = publish_down

    def set_trash(self, trash):
        self._trash = trash

    def set_access(self, access):
        self._access = access

    def set_ordering(self, ordering):
        self._ordering = ordering

    def set_featured(self, featured):
        self._featured = featured

    def set_featured_ordering(self, featured_ordering):
        self._featured_ordering = featured_ordering

    def set_image_caption(self, image_caption):
        self._image_caption = image_caption

    def set_image_credits(self, image_credits):
        self._image_credits = image_credits

    def set_video_caption(self, video_caption):
        self._video_caption = video_caption

    def set_video_credits(self, video_credits):
        self._video_credits = video_credits

    def set_hits(self, hits):
        self._hits = hits

    def set_params(self, param):
        self._param = param

    def set_metadesc(self, metadesc):
        self._metadesc = metadesc

    def set_metadata(self, metadata):
        self._metadata = metadata

    def set_metakey(self, metakey):
        self._metakey = metakey

    def set_plugins(self, plugins):
        self._plugins = plugins

    def set_language(self, language):
        self._language = language
