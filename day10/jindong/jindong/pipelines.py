# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JindongPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(port=33061, host="127.0.0.1", user="root", passwd="xiangzong30917", db="shanpin")
        curson=conn.cursor()
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            shop=item["shop"][i]

            curson.execute("insert into goods(title,shop) values('{}', '{}')".format(title, shop))
            conn.commit()
        conn.close()

        # return item
