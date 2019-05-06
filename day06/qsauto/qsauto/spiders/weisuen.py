# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import QsautoItem
import re
import urllib.request
from scrapy.http import Request



class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://www.qiushibaike.com/']


    rules = (
        Rule(LinkExtractor(allow='article'), callback='self.parse_item', follow=True,),
    )
    def start_requests(self):
        ua={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    "Chrome/30.0.1599.101 Safari/537.36"}
        yield Request("https://www.qiushibaike.com/", headers=ua)

    def parse_item(self, response):
        i = QsautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i["content"]=response.xpath('//div[@class="content"]/text()').extract()
        i["link"]=response.xpath('//link[@rel="canonical"]/@href').extract()
        print(i["content"])
        print(i["link"])
        return i

