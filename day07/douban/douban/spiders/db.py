# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request
import re

class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    "Chrome/30.0.1599.101 Safari/537.36"}
    '''
    start_urls = (
        'http://www.douban.com/',
    )'''
    def start_requests(self):
        return [Request("https://accounts.douban.com/login", callback=self.parse, meta={"cookiejar":1})]

    def parse(self, response):
        # captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()
        pagedata=urllib.request.urlopen("https://accounts.douban.com/login").read()
        pagedata=pagedata.decode("utf-8","ignore")
        captcha=re.compile(r'<img id="captcha_image" src="(.*?)"').findall(pagedata)
        url = r'https://accounts.douban.com/login'
        print(len(captcha))
        print("*****")
        if len(captcha)>0:
            localPath="F:/Python/爬虫与数据分析/day07/验证码图片/captcha.png"
            urllib.request.urlretrieve(captcha[0], filename=localPath)
            print("请查看本地验证码图片并输入验证码:")
            captcha_value=input()
            data={
                "form_email": "987727555@qq.com",
                "form_password": "xiangzong30917",
                "captcha-solution":captcha_value,
                "redir": "https://www.douban.com/people/184603739/",
            }

        else:
            print("此时没有验证码")
            data={
                "form_email": "987727555@qq.com",
                "form_password": "xiangzong30917",
                "redir": "https://www.douban.com/people/184603739/",
            }
        print("登录中....")
        print(data)
        return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]}, headers=self.header, formdata=data, callback=self.next,)]

    def next(self, response):
        print("*****")
        print("此时已经登录完成并爬取了个人中心的数据")
        title=response.xpath("/html/head/title/text()").extract()
        print(title[0])

