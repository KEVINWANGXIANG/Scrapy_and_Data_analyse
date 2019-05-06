
import urllib.request
import urllib.error
import os,re

url=r"https://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36")
opener=urllib.request.build_opener()
opener.add_handler=[headers]
#print('123')
data=opener.open(url).read().decode("utf-8", "ignore")
# print(len(data))
# with open(r"F:\Python\爬虫与数据分析\day02\file4.html","wb") as f:
#     f.write(data)
# f.close()
#<a href="https://gitbook.cn/gitchat/column/5b444ae6
# 94c0f60b4ec4a68c?utm_source=feed18058" target="_blank"><p class
# ="tit">完美架构探索——分布式微服务架构体系详解</p><p class="intro">本课程会一一解
# 开微服务架构下分布式场景的问题，以及通过对于一些分布式技术的原理、模型和算法的介绍，
# 来帮助想要实施微服务架构的工程师们知其然并知其所以然。……</p></a>
pat=r'<dd class="name">\n<a href="(.*?)"target="_blank">'
allUrls=re.compile(pat).findall(data)
print(len(allUrls))
# print(allUrls)
for i in range(0,len(allUrls)):
    try:
        print("这是第%d次爬取" %(i+1))
        thisurl=allUrls[i]
        print(thisurl)
        file=r"F:/Python/爬虫与数据分析/day02/csdn网页文章/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,filename=file)
        print("爬取成功")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except Exception as e:
        print("爬取出错")