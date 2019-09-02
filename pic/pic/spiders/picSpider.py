import scrapy
from pic.items import PicItem

class XhSpider(scrapy.Spider):
    name = "xh"
    start_urls = [
        "http://www.xiaohuar.com/list-1-1.html"
    ]

    def parse(self, response):
        allPics = response.xpath("//div[@class='img']/a")
        for pic in allPics:
            item = PicItem()
            name = pic.xpath("./img/@alt").extract()[0]
            addr = pic.xpath("./img/@src").extract()[0]
            addr = "http://www.xiaohuar.com" + addr
            item["name"] = name
            item["addr"] = addr
            yield item