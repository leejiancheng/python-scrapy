import os
import random
import requests
from bs4 import BeautifulSoup

UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {
    "User-Agent": random.choice(UserAgent_List),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip"
}

def get_page(pageNum):
    url = "http://www.meizitu.com/a/cute_{0}.html".format(pageNum)
    html = requests.get(url)
    html.encoding = "gb2312"
    text = html.text
    bsop = BeautifulSoup(text, "html.parser")
    img_list = bsop.find("ul", {"class": "wp-list clearfix"}).findAll("a")
    url_list = []
    s = set()
    for img in img_list:
        if (img.attrs["href"] in s):
            continue
        url_list.append(img.attrs["href"])
        s.add(img.attrs["href"])
    return url_list

def get_img(url):
    html = requests.get(url)
    html.encoding = "gb2312"
    text = html.text
    bsop = BeautifulSoup(text, "html.parser")
    imgs = bsop.find("div", {"id": "picture"}).findAll("img")
    img_title = bsop.find("div", {"class": "metaRight"}).find("a").string
    os.mkdir(img_title)
    count = 1
    for img in imgs:
        img_url = img.attrs["src"]
        filename = "{0}/{1}/{2}.jpg".format(os.path.abspath("."), img_title, count)
        with open(filename, "wb+") as jpg:
            jpg.write(requests.get(img_url, headers=headers).content)
        print("正在抓取{0}的第{1}张图片".format(img_title, count))
        count += 1

if __name__ == "__main__":
    print(u"正在爬取 http://www.meizitu.com 的图片")
    pageNum = input(u"请输入要爬取的页码：")
    print("---------正在爬取中---------")
    urls = get_page(pageNum)
    for url in urls:
        print("===============")
        get_img(url)
        print("===============")
    print("---------爬取完毕---------")