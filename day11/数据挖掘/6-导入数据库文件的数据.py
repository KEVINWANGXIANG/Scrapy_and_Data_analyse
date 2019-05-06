
import pymysql
import pandas

conn = pymysql.connect(host="127.0.0.1", port=33061, user="root", passwd="xiangzong30917", db="shanpin")
# sql = "select * from goods WHERE shop='安踏官方旗舰店'"
# data = pandas.read_sql(sql, conn)
# data = pandas.read_sql("select CAST(SUBSTRING(DT_DATE,9,2) AS SIGNED) DT_DATE,HIGH_TEMP,LOW_TEMP from tb", con=conn)
data = pandas.read_sql("select title, shop from goods", con=conn)
print(data)

















