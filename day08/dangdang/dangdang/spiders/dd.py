# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = (
        'http://www.dangdang.com/',
    )

    def parse(self, response):
        item=DangdangItem()
        item["title"]=response.xpath('//a[@name="itemlist-title"]/@title').extract()
        item["link"]=response.xpath('//a[@name="itemlist-title"]/@href').extract()
        item["comment"]=response.xpath('//a[@class="search_comment_num"]/text()').extract()
        yield item
        for i in range(2, 10):
            #http://category.dangdang.com/pg2-cp01.54.06.19.00.00.html
            url='http://category.dangdang.com/pg'+str(i)+'-cp01.54.06.19.00.00.html'
            yield Request(url, callback=self.parse)


