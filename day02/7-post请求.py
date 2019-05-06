
import urllib.request
import urllib.parse

url="http://www.baidu.com/mypost/"
mydata=urllib.parse.urlencode({
    "name":"kevin",
    "passwd":"123456",
}).encode("utf-8")
req=urllib.request.Request(url, mydata)
response=urllib.request.urlopen(req)
data=response.read()
with open(r"F:\Python\爬虫与数据分析\day02\file3.html","wb") as f:
    f.write(data)

f.close()




