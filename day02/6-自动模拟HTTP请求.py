
import urllib.request
import re

keywd="王祥"
keywd=urllib.request.quote(keywd)
url="http://www.baidu.com/s?wd="+keywd+"ie=utf-8&tn=88093251_21_hao_pg"
req=urllib.request.Request(url)

data=urllib.request.urlopen(req).read()

print(len(data))
# with open(r"F:\Python\爬虫与数据分析\day02\file2.html","wb") as f:
#     f.write(data)
# f.close()
