# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re,os
from scrapy.http import Request
from lxml import etree
from jindong.items import JindongItem
import requests
import lxml

class GoodsSpider(scrapy.Spider):
    name = "goods"
    allowed_domains = ["jd.com"]
    start_urls = (
        'http://www.jd.com/',
    )

    def parse(self, response):
        item=JindongItem()
        key=input("请输入您要搜索的鞋子品牌:")
        keyname=urllib.request.quote(key)
        # print(keyname)
        for i in range(2,11):
            url=r'https://search.jd.com/Search?keyword='+keyname+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&ev=exbrand_'+keyname+'%EF%BC%88ANTA%EF%BC%89%5E&page='+str(2*i-1)+'&s='+str(53*i-44)+'&click=0'
            # print(url)
            # url_zong_list=response.xpath('//div[@class="p-img"]/a/@href').extract()
            edit_web=requests.get(url)
            edit_web.encoding="utf-8"
            selector = etree.HTML(edit_web.text)
            url_zong_list=selector.xpath('//div[@class="p-img"]/a/@href')
            # print(url_zong_list)
            for detail_url in url_zong_list:
                try:
                    '''
                    detail_url='http:'+detail_url
                    # print(detail_url)
                    detail_data=urllib.request.urlopen(detail_url).read().decode("utf-8", "ignore")
                    title_pat=r'<div class="item ellipsis" title="(.*?)">'
                    title=re.compile(title_pat).findall(detail_data)
                    print(title[0])
                    print("--------------------")
                    '''
                    # print(detail_url)
                    detail_url='http:'+detail_url
                    print(detail_url)
                    detail_edit_web = requests.get(detail_url)
                    detail_edit_web.encoding="utf-8"
                    selector_detail_url_title=etree.HTML(detail_edit_web.content)
                    title=selector_detail_url_title.xpath("//html/head/title/text()")
                    # title=title[0]
                    item["title"]=title
                    print(title)

                    selector_detail_url_shop=etree.HTML(detail_edit_web.content)
                    shop=selector_detail_url_shop.xpath('//div[@class="name"]/a/@title')
                    # shop=shop[0]
                    item["shop"]=shop
                    print(shop)

                    yield item


                    # item["title"]=title
                    # print(item["title"])
                except Exception as e:
                    print("爬取失败")
                    pass



