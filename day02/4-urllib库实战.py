
import urllib.request

# urllib.request.urlretrieve(r"http://www.baidu.com",filename=r"F:\Python\爬虫与数据分析\day02\file1.html")
# urllib.request.urlcleanup()

file=urllib.request.urlopen("http://www.baidu.com")
# print(file.info())

print(file.getcode())

print(file.geturl())




