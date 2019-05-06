
from scrapy.spiders import Spider
import scrapy
class FirstSpider(Spider):
    name="first"
    allowed_domains=["baidu.com"]
    start_urls=["http://www.baidu.com", ]
    #回调函数
    def parse(self, response):
        pass







































