# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jindong.items import JindongItem
import re
import urllib.request
from scrapy.http import Request


class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )
    def start_requests(self):
        return [Request("http://www.jd.com/", callback=self.parse_item, meta={"cookiejar":1})]
    # def start_requests(self):
    #     ua={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
    # "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    # "Chrome/30.0.1599.101 Safari/537.36"}
    #     yield Request("https://item.jd.com/", headers=ua)
    def parse_item(self, response):
        print("&&&&&&&&&&&")
        try:
            i = JindongItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            # return i
            thisurl=response.url
            print(thisurl)
            pat='item.jd.com/(.*?).html'
            x=re.search(pat, thisurl)
            print("****")
            print(x)
            if x:
                print("hello")
                thisid=re.compile(pat).findall(thisurl)[0]
                print(thisid)
                title=response.xpath("//html/head/title/text()").extract()
                shop=response.xpath('//div[@class="name"]/a/@title').extract()
                shoplink=response.xpath('//div[@class="name"]/a/@href').extract()
                print(title)
                print(shop)
                print(shoplink)
#价格https://c0.3.cn/stock?skuId=7019143&area=1_72_2799_0&venderId=1000000127&cat=670,671,2694&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=15372732187711552157291&pdpin=&detailedAdd=null&callback=jQuery8417868
                #7019143
                priceurl='https://c0.3.cn/stock?skuId='+str(thisid)+'&area=1_72_2799_0&venderId=1000000127&cat=670,671,2694&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=15372732187711552157291&pdpin=&detailedAdd=null&callback=jQuery8417868'
                pricedata=urllib.request.urlopen(priceurl).read().decode("utf-8","ignore")
                pricepat='"p":"(.*?)"'
                price=re.compile(pricepat).findall(pricedata)
                if len(title) and len(shop) and len(shoplink) and len(price):
                    print(title[0])
                    print(shop[0])
                    print(shoplink[0])
                    print(price[0])
                else:
                    pass
            else:
                print("处理出错")
            return i
        except Exception as e:
            print(e)

