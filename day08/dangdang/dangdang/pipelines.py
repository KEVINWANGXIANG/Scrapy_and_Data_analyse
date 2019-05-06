# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1", user="root", passwd="xiangzong", db="dd")
        curson=conn.cursor()
        # sql = "insert into books(title,link,comment) values('1','2','3')"
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            # print(title)
            # print(link)
            # print(comment)
            # sql = "insert into books(title,link,comment) values(title,link,comment)"
            #sql = "insert into books(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            #sql = "insert into books(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"

            curson.execute("insert into books(title,link,comment) values('{}', '{}', '{}')".format(title, link, comment))
        # sql="select * from books where link='http://product.dangdang.com/25242552.html'"
        # curson.execute(sql)
        # conn.query(sql)
            conn.commit()
        conn.close()
        # print("*****")
        # return item

