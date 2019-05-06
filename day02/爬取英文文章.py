
import urllib.request
import re
import os
import urllib.error
import ssl

headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    "Chrome/30.0.1599.101 Safari/537.36"
    }
page_num = 1
url_all = []

for i in range(65, 80, 1):
    page_url = r'http://www.dioenglish.com/home.php?mod=space&do=blog&view=all&page=' + str(i)
    req = urllib.request.Request(page_url, headers=headers)
    response = urllib.request.urlopen(req)
    pagedata = response.read().decode("utf-8", 'ignore')
    pat1 = r'>Shares</a>\n<a href="(.*?)" target="_blank">'
    urlList = re.compile(pat1, re.S).findall(pagedata)
    print(len(urlList))
    # page_num += 1
    url_all.append(urlList)
url_all_outer = []
for i in range(len(url_all)):
    if len(url_all[i]) == 0:
        continue
    for j in range(len(url_all[i])):
        this_url = url_all[i][j]
        this_url = this_url.replace('amp;', '')
        # print(this_url)
        url_all_outer.append(this_url)
print(len(url_all_outer))
true_url = []
text_num = 1
for k in range(0, len(url_all_outer)):
    thisUrl = url_all_outer[k]
    # print(thisUrl)
    req = urllib.request.Request(thisUrl, headers=headers)
    response = urllib.request.urlopen(req)
    article_data = response.read().decode("utf-8", 'ignore')
    # print(article_data)
    # pat2 = r'<a id="share_space"(.*?)</span>'
    # pat2 = '<a id="share_space"(.*?)</span>'
    pat2 = '<a id="share_space" href="(.*?)</span>'
    true_article_url = re.compile(pat2, re.S).findall(article_data)
    pat3 = r'<a href="(.*?)">'
    art = re.compile(pat3, re.S).findall(true_article_url[0])
    # print(true_article_url)
    # print(art)
    art = str(art[0])
    true_url.append(art)
# print(len(true_url))
print(true_url)
text_num = 415
for i in range(500):
    true_article_data = urllib.request.urlopen(true_url[i]).read().decode("utf-8", "ignore")
    # true_article_data = urllib.request.urlopen(true_article_url).read().decode("utf-8","ignore")
    toPath = os.path.join('D:/文章/1', str(text_num) + ".xml")
    text_num += 1

    with open(toPath, "w", encoding="utf-8") as f:
        f.write(true_article_data)
    print("第%d个文档写入成功" % (text_num - 1))








'''
http://www.dioenglish.com/home.php?mod=space&amp;uid=26284&amp;do=blog&amp;id=57354
http://www.dioenglish.com/home.php?mod=space&uid=44409&do=blog&id=57374
http://www.dioenglish.com/home.php?mod=space& uid=26284&do=blog&id=57354
'''
'''
text_num = 1
for k in range(0, len(urlList)):
    thisUrl = urlList[k]
    req = urllib.request.Request(thisUrl, headers=headers)
    response = urllib.request.urlopen(req)
    article_data = response.read().decode("utf-8", 'ignore')
    # toPath = r"D:/文章" + str(text_num) + ".txt"
    pat2 = r'<a href="https://coolshell.cn/wp-login.php">登录</a></li>\n			<li><a href="(.*?)">文章'
    true_article_url = re.compile(pat2, re.S).findall(article_data)
    print(true_article_url)
'''
    # ssl._create_default_https_context = ssl._create_unverified_context
    # req = urllib.request.Request(true_article_url, headers=headers)
    # response = urllib.request.urlopen(req)

'''
    true_article_data = urllib.request.urlopen(true_article_url[0]).read().decode("utf-8", "ignore")
    # true_article_data = urllib.request.urlopen(true_article_url).read().decode("utf-8","ignore")
    toPath = os.path.join('D:/文章', str(text_num) + ".txt")
    text_num += 1
    with open(toPath, "w", encoding="utf-8") as f:
        f.write(true_article_data)
    print("第%d个文档写入成功" % (text_num - 1))
print(text_num)
'''


'''
text_num = 1
for i in range(1, 21):
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
            toPath = r"C:/Users/Administrator/Desktop/文章" + str(text_num) + ".txt"
            toPath = os.path.join('C:/Users/Administrator/Desktop/文章', str(text_num) + ".txt")
            text_num += 1
            with open(toPath, "w", encoding="utf-8") as f:
                f.write(article_List[k])
            print("第%d个文档写入成功" %(text_num - 1))
'''



