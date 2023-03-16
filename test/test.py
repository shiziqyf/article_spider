import ssl

import requests

# ssl._create_default_https_context = ssl._create_unverified_context


def urllib_download(url):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('img.png', 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


if __name__ == '__main__':
    urllib_download("https://s2.loli.net/2023/03/05/qigmFrL4U7I5WbA.png")
