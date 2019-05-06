
import urllib.request

url="http://d1.weather.com.cn/calendar_new/2018/101270101_201809.html?_=1537945808020"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36")
opener=urllib.request.build_opener()
opener.add_handle=[headers]
data=opener.open(url).read()
print(data)
# with open(r"F:\Python\爬虫与数据分析\day02\file3.html","wb") as f:
#     f.write(data)
# f.close()








