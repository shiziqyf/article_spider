import os
import ssl

import requests

from spider import common
from spider.server import oss_service


# ssl._create_default_https_context = ssl._create_unverified_context


def urllib_download(url):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        folder_path = '/Users/developer/Desktop/cache/img'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        open(folder_path + '/test', 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


def download_from_url(url):
    start = common.get_current_time()
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    resp = requests.get(url, headers=headers, timeout=1)

    print("resp.content = ", len(resp.content))
    print("Content-Length = ", resp.headers['Content-Length'])
    oss_key = oss_service.upload_to_oss('test22222.jpg', resp)
    end = common.get_current_time()
    print("rt = ", end - start)

if __name__ == '__main__':
    url = 'https://cdn-img.msdniso.com/2023-03-20/_1679241904005_550'
    download_from_url(url)
    # urllib_download("https://s2.loli.net/2023/03/05/qigmFrL4U7I5WbA.png")
