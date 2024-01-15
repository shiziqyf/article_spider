import requests
from lxml import etree
from lxml.html import tostring

def download_today_img():
    page = 100
    while (page < 1000):
        url = 'https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count,sender,album,msg,reply_count,top_comments&kw=%E5%A4%B4%E5%83%8F&start='+str(page)+'&_=1705287225867'
        response = requests.get(url, timeout=60)
        resp_json = response.json()
        object_list = resp_json['data']['object_list']
        for object in object_list:
            url = object['photo']['path']
            id = object['photo']['id']
            print(url)
        #         end_date = img['enddate']
        #         urlbase = img['urlbase']
        #         url = 'https://www.bing.com/' + urlbase + "_UHD.jpg&pid=hp&w=3840&h=2160&rs=1&c=4"
            download_from_url(url, str(id) + ".jpg")
        page = page + 24



def get_from_github():
    url = 'https://github.com/niumoo/bing-wallpaper/tree/main/picture/2023-02'
    response = requests.get(url, timeout=60)
    content = response.content.decode('utf-8', 'ignore')
    root = etree.HTML(content)
    td_elements = root.xpath('//table/tbody//td')
    for td in td_elements:
        try:
            urls = td.xpath('./a[2]/@href')
            names = td.xpath('./text()')
            url = ''
            name = ''
            if len(urls) > 0:
                url = urls[0] + '&pid=hp&w=3840&h=2160&rs=1&c=4'
            if len(names) > 0:
                name = names[0].replace('-', '').replace(' ', '') + ".jpg"
            download_from_url(url, name)
        except Exception:
            print('error...')
    # for url in urls:
    #     print(url)
def download_from_url(url, name):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    resp = requests.get(url, headers=headers, stream=True, timeout=60)
    folder_path = '/Users/developer/Desktop/wallper/avatar/' + name
    open(folder_path, 'wb').write(resp.content)  # 将内容写入图片
    print("success: url=%s, name=%s" % (url, name))




if __name__ == '__main__':
    download_today_img()
    # get_from_github()