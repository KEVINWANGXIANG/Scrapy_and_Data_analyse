import urllib.request
import re,os

data=urllib.request.urlopen("https://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
#<a target="_blank" href="http://news.sina.com.cn/
# c/gat/2018-09-05/doc-ifxeuwwr4142345.shtml">日本关西机场被淹 中使馆接人台同胞这样问</a>
pat=r'<a target="_blank" href="(.*?)"'
allurls=re.compile(pat).findall(data2)
print(len(allurls))
for i in range(0,len(allurls)):
    try:
        print("这是第%d次爬取" %(i+1))
        thisurl=allurls[i]
        # print(thisurl)
        file=r"F:/Python/爬虫与数据分析/day02/新闻网页/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl, filename=file)
        print("爬取成功")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
