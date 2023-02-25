class Article:
    def __init__(self, origin_url, content_pack='', source=''):
        self._origin_url = origin_url
        self._content_pack = content_pack
        self._source = source

    @property
    def source_url(self):
        return self._origin_url

    @property
    def content_pack(self):
        return self._content_pack

    @property
    def source(self):
        return self._source

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

# class Content:
#     def __init__(self, url='', title='', content=''):
#         self._url = url
#         self._title = title
#         self._content = content
#
#
