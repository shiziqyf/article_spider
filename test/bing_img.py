import requests


def download_today_img():
    url = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    response = requests.get(url, timeout=60)
    resp_json = response.json()
    images = resp_json['images']
    for img in images:
        end_date = img['enddate']
        urlbase = img['urlbase']
        url = 'https://www.bing.com/' + urlbase + "_UHD.jpg&pid=hp&w=3840&h=2160&rs=1&c=4"
        download_from_url(url, end_date + ".jpg")


def download_from_url(url, name):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    resp = requests.get(url, headers=headers, stream=True, timeout=60)
    folder_path = '/Users/developer/Desktop/wallper/bing/' + name
    open(folder_path, 'wb').write(resp.content)  # 将内容写入图片
    print("success: url=%s, name=%s" % (url, name))


if __name__ == '__main__':
    download_today_img()
