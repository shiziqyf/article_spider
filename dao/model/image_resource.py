class ImageResource:
    def __init__(self, id=None, url=None, oss_key=None, from_task_id=None, gmt_created_time=None, gmt_updated_time=None, from_article_resource_id=None):
        self.id = id
        self.url = url
        self.oss_key = oss_key
        self.from_task_id = from_task_id
        self.from_article_resource_id = from_article_resource_id
        self.gmt_created_time = gmt_created_time
        self.gmt_updated_time = gmt_updated_time
