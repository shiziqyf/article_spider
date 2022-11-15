class Article:
    def __init__(self, content='', source='', created=0, updated=0):
        self._content = content
        self._source = source
        self._created = created
        self._updated = updated

    @property
    def content(self):
        return self._content

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
