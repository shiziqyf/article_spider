import traceback

import oss2

import global_var
from config import settings
from spider import common

auth = None
img_bucket = None


def init():
    global auth
    global img_bucket
    auth = oss2.Auth(settings.oss.access_key, settings.oss.access_secret)
    img_bucket = oss2.Bucket(auth, settings.oss.endpoint, settings.oss.img_bucket)


def upload_network_stream(url, stream):
    biz_log = global_var.get_value('biz_log')
    key = settings.oss.prefix + common.get_today_time_str() + "/" + common.generate_random_id()
    try:
        upload_resp = img_bucket.put_object(key, stream)
        if upload_resp.status != 200:
            biz_log.error('upload_network_stream fail, url=%s, resp=%s', url, upload_resp)
            raise Exception('upload_network_stream fail')
        return key
    except Exception:
        biz_log.error('upload_network_stream fail, url=%s, e=%s', url, traceback.format_exc())
        raise Exception('upload_network_stream fail')

def exist(key):
    return img_bucket.object_exists(key)
