# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["content"])):
            print(item["content"][i])
            print(item["link"][i])






        # print(item["content"])
        # with open(r'F:\Python\爬虫与数据分析\day06\first\file.txt',"w",encoding="utf-8") as f:
        #     f.write(item["content"])
        return item

