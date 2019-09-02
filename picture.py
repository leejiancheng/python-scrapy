import re
import os
import requests

url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%B1%A1%20%E8%A1%A8%E6%83%85%E5%8C%85"
pic_file_path = os.path.join(os.path.abspath("."), "picture")
i = 0

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

if not os.path.exists(pic_file_path):
    os.makedirs(pic_file_path)

for item in pic_url:
    print("正在下载图片: ", item)
    try:
        pic = requests.get(item, allow_redirects=False, timeout=10)
    except requests.exceptions.ConnectionError:
        print("【错误】当前图片无法下载")
        continue
    img_name = "{0}.jpg".format(i)
    file_path = os.path.join(pic_file_path, img_name)
    with open(file_path, "wb") as f:
        f.write(pic.content)
    i += 1