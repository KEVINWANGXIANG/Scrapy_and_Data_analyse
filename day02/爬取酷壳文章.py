
import urllib.request
import re
import os
import urllib.error
import ssl

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    "Chrome/30.0.1599.101 Safari/537.36"
    }


text_num = 126
for i in range(35, 60):
    #https://www.qiushibaike.com/8hr/page/3/
    #https://www.qiushibaike.com/text/page/3/
    url='https://www.qiushibaike.com/text/page/' + str(i)
    req=urllib.request.Request(url, headers=headers)
    response=urllib.request.urlopen(req)
    # pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pagedata=response.read().decode("utf-8", 'ignore')
    # print(pagedata)
    pat1 = r'</div>\n\n<a href="(.*?)" target="_blank" class="contentHerf"'
    urlList = re.compile(pat1, re.S).findall(pagedata)
    # print(urlList)
    # for j in range(0,len(datalist)):
    #     print("第"+str(i)+"页"+"第"+str(j+1)+"个段子的内容是:")
    #     print(datalist[j])
    # print(len(urlList))
    for j in range(0, len(urlList)):
        # print("第" + str(i) + "页" + "第" + str(j + 1) + "个段子的内容是:")
        # print(urlList[j])
        url_article = 'https://www.qiushibaike.com' + urlList[j]
        req=urllib.request.Request(url_article, headers=headers)
        response=urllib.request.urlopen(req)
        # pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        article_data=response.read().decode("utf-8", 'ignore')
        pat2 = r'<div class="content">(.*?)</div>'
        article_List = re.compile(pat2, re.S).findall(article_data)
        for k in range(0, len(article_List)):
            toPath = r"C:/Users/Administrator/Desktop/中文文档500篇" + str(text_num) + ".txt"
            toPath = os.path.join('C:/Users/Administrator/Desktop/中文文档500篇', str(text_num) + ".txt")
            text_num += 1
            with open(toPath, "w", encoding="utf-8") as f:
                f.write(article_List[k])
            print("第%d个文档写入成功" % (text_num - 1))




