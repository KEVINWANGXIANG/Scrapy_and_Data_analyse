import urllib.request
import os,re


url = r"https://read.douban.com/provider/all"
path=r"F:\Python\爬虫与数据分析\day02\file.html"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
req=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(req)
HtmlStr=response.read().decode("utf-8")
# with open(path,"w",encoding="utf-8") as f:
#     f.write(HtmlStr)
# <div class="name">北京邮电大学出版社</div>
pat=r'<div class="name">(.*?)</div>'
re_publish=re.compile(pat)
data=re_publish.findall(HtmlStr)
# print(data)
toPath=r"F:\Python\爬虫与数据分析\day02\file.txt"
for pub in data:
    with open(toPath, "a", encoding="utf-8") as f:
        f.write(pub+"\n")