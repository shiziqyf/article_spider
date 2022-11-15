class Article:
    def __init__(self, title='', content='', source='', created=0, updated=0):
        self._title = title
        self._content = content
        self._source = source
        self._created = created
        self._updated = updated

    @property
    def title(self):
        return self._title

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
