# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request
from pic import settings

class PicPipeline(object):
    def process_item(self, item, spider):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Referer": "http://www.xiaohuar.com/list-1-1.html"
        }
        dir_path = "{0}/{1}".format(settings.IMAGES_STORE, spider.name)
        # print(item["addr"])
        req = urllib.request.Request(url=item["addr"], headers=headers)
        res = urllib.request.urlopen(req)
        # pic_name = item["name"] + ".jpg"
        file_name = "{0}/{1}.jpg".format(dir_path, item["name"])

        # file_name = os.path.join("F:/pic", item["name"] + ".jpg")
        with open(file_name, "wb") as fire_writer:
            fire_writer.write(res.read())
        return item
