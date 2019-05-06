# -*- coding: utf-8 -*-
import scrapy
from houseInfo.items import HouseinfoItem
import re
import urllib.request
from lxml import etree
import requests

class HouseSpider(scrapy.Spider):
    name = "house"
    allowed_domains = ["zu.fang.com"]
    start_urls = (
        'http://www.zu.fang.com/',
    )

    def parse(self, response):
        item=HouseinfoItem()
        #http://zu.fang.com/house/i35/
        for i in range(1, 9):
            url=r'http://zu.fang.com/house/i3' + str(i) + '/'
            # print(url)
            # url_zong_list=response.xpath('//div[@class="p-img"]/a/@href').extract()
            edit_web=requests.get(url)
            edit_web.encoding="utf-8"
            selector = etree.HTML(edit_web.text)
            url_zong_list=selector.xpath('//p[@class="title"]/a/@href')
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
                    detail_url='http://zu.fang.com'+ detail_url
                    print(detail_url)
                    detail_edit_web = requests.get(detail_url)
                    detail_edit_web.encoding="utf-8"
                    selector_detail_url_title=etree.HTML(detail_edit_web.content)
                    title=selector_detail_url_title.xpath("//html/head/title/text()")
                    # title=title[0]
                    item["title"]=title
                    print(title)


                    # data=urllib.request.urlopen(detail_url).read().decode("utf-8", "ignore")
                    # # print(data)
                    # pat=r'<div class="tt">(.*?)</div>'
                    # housesize=re.compile(pat).findall(data)
                    # print(housesize)

                    selector_detail_url_housesize=etree.HTML(detail_edit_web.content)
                    housesize=selector_detail_url_housesize.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()')
                    housesize=housesize[0]
                    housesize=str(housesize)
                    housesize=re.sub("\D", "", housesize)
                    print(housesize)
                    item["housesize"]=housesize
                    # print(type(housesize))
                    # shop=shop[0]
                    # item["shop"]=shop
                    # print(shop)

                    selector_detail_url_price=etree.HTML(detail_edit_web.content)
                    price=selector_detail_url_price.xpath('//span[@class="zf_mianji"]/b/text()')
                    print(price)
                    item["price"]=price


                    yield item
                except Exception as e:
                    print("爬取失败")
                    pass


            '''
            try:
                url=r'http://zu.fang.com/house/i3' + str(i) + '/'
                print(url)
                edit_web=requests.get(url)
                edit_web.encoding="utf-8"
                selector = etree.HTML(edit_web.content)
                title=selector.xpath('//p[@class="title"]/a/text()')
                # title=title[0]
                item["title"]=title
                # print(title)

                # housesize=selector.xpath('//class="font15 mt12 bold"/')

                headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36")
                opener=urllib.request.build_opener()
                opener.add_handler=[headers]
                data=opener.open(url).read().decode("utf-8", "ignore")
                pat=r'<span class="splitline">|</span>.*?<span class="splitline">|</span>(.*)㎡<span class="splitline">|</span>'
                housesize=re.compile(pat).findall(data)

                print(housesize)
                # yield item


                # item["title"]=title
                # print(item["title"])
            except Exception as e:
                print("爬取失败")
                pass
            '''