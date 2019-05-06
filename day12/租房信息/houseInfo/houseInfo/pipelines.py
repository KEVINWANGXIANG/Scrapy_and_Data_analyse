# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HouseinfoPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(port=33061, host="127.0.0.1", user="root", passwd="xiangzong30917", db="houseinfo")
        curson=conn.cursor()
        for i in range(0, len(item["title"])):
            title=item["title"][i]
            housesize=item["housesize"][i]
            price=item["price"][i]
            curson.execute("insert into house(title,housesize,price) values('{}', '{}','{}')".format(title, housesize, price))
            conn.commit()
        conn.close()
