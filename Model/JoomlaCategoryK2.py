class JoomlaCategoryK2(object):
    
    def __init__(self, data):

        self._id = data['id']
        self._name = data['name']
        self._alias = data['alias']
        self._description = data['description']
        self._parent = data['parent']
        self._extraFieldsGroup = data['extraFieldsGroup']
        self._published = data['published']
        self._access = data['access']
        self._ordering = data['ordering']
        self._image = data['image']
        self._params = data['params']
        self._trash = data['trash']
        self._plugins = data['plugins']
        self._language = data['language']

    # gets #

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_alias(self):
        return self._alias

    def get_description(self):
        return self._description

    def get_parent(self):
        return self._parent

    def get_extraFieldsGroup(self):
        return self._extraFieldsGroup

    def get_published(self):
        return self._published

    def get_access(self):
        return self._access

    def get_ordering(self):
        return self._ordering

    def get_image(self):
        return self._image

    def get_params(self):
        return self._params

    def get_trash(self):
        return self._trash

    def get_plugins(self):
        return self._plugins

    def get_language(self):
        return self._language

    # sets #

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_alias(self, alias):
        self._alias = alias

    def set_description(self, description):
        self._description = description

    def set_parent(self, parent):
        self._parent = parent

    def set_extraFieldsGroup(self, extraFieldsGroup):
        self._extraFieldsGroup = extraFieldsGroup

    def set_published(self, published):
        self._published = published

    def set_access(self, access):
        self._access = access

    def set_ordering(self, ordering):
        self._ordering = ordering

    def set_image(self, image):
        self._image = image

    def set_params(self, params):
        self._params = params

    def set_trash(self, trash):
        self._trash = trash

    def set_plugins(self, plugins):
        self._plugins = plugins

    def set_language(self, language):
        self._language = language



