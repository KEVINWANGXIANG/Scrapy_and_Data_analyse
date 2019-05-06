import threading
import urllib.request
import re,os
import urllib.error

'''
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,30):
            print("我是线程A")

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,30):
            print("我是线程B")

t1=A()
t1.start()
t2=B()
t2.start()
'''
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
    "Chrome/30.0.1599.101 Safari/537.36"
    }
#headers=("User-Agent","User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)")
# opener=urllib.request.build_opener()
# opener.add_handle=[headers]
# urllib.request.install_opener(opener)
class one(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,7,2):
    #https://www.qiushibaike.com/8hr/page/3/
            url='https://www.qiushibaike.com/8hr/page/'+str(i)
            req=urllib.request.Request(url,headers=headers)
            response=urllib.request.urlopen(req)
    # pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
            pagedata=response.read().decode("utf-8")
    # print(pagedata)
            pat=r'<div class="content">\n<span>(.*?)</span>'
            datalist=re.compile(pat,re.S).findall(pagedata)
    # print(len(datalist))
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页"+"第"+str(j+1)+"个段子的内容是:")
                print(datalist[j])

class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2,7,2):
    #https://www.qiushibaike.com/8hr/page/3/
            url='https://www.qiushibaike.com/8hr/page/'+str(i)
            req=urllib.request.Request(url,headers=headers)
            response=urllib.request.urlopen(req)
    # pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
            pagedata=response.read().decode("utf-8")
    # print(pagedata)
            pat=r'<div class="content">\n<span>(.*?)</span>'
            datalist=re.compile(pat,re.S).findall(pagedata)
    # print(len(datalist))
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页"+"第"+str(j+1)+"个段子的内容是:")
                print(datalist[j])

t1=one()
t1.start()
t2=Two()
t2.start()







