
import re,os
import urllib.request
import time
import urllib.error

def use_proxy(proxy_addr, url):
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')
        proxy=urllib.request.ProxyHandler({"http":proxy_addr})
        opener=urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(req).read().decode("utf-8", "ignore")
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

'''
https://weixin.sogou.com/weixin?query=python&_sug_type_=&sut=2345&lkt=7%2C1536736051129%2C1536736053327&s_from=input&_sug_=y&type=2&sst0=1536736053539&page=2&ie=utf8&w=01019900&dr=1
https://weixin.sogou.com/weixin?query=python&_sug_type_=&sut=2345&lkt=7%2C1536736051129%2C1536736053327&s_from=input&_sug_=y&type=2&sst0=1536736053539&page=3&ie=utf8&w=01019900&dr=1
http://mp.weixin.qq.com/s?src=11&timestamp=1536736085&ver=1117&signature=uPU-E3cysQcIULZ4R6llc9nFrPWek56Wi0mR7Qmp8INDRL9QutzblK525rpvzn0iLcCt*kjTlRicgx*t2Zvj*WNTdaGB9VTNxcvBi4q1QZqQzGyAF9t0hvcpPPBU7P8T&new=1
https://mp.weixin.qq.com/s?src=11&timestamp=1536736085&ver=1117&signature=uPU-E3cysQcIULZ4R6llc9nFrPWek56Wi0mR7Qmp8INDRL9QutzblK525rpvzn0iLcCt*kjTlRicgx*t2Zvj*WNTdaGB9VTNxcvBi4q1QZqQzGyAF9t0hvcpPPBU7P8T&new=1
http://mp.weixin.qq.com/s?src=11&amp;timestamp=1536736085&amp;ver=1117&amp;signature=uPU-E3cysQcIULZ4R6llc9nFrPWek56Wi0mR7Qmp8INDRL9QutzblK525rpvzn0iLcCt*kjTlRicgx*t2Zvj*WNTdaGB9VTNxcvBi4q1QZqQzGyAF9t0hvcpPPBU7P8T&amp;new=1
'''

key="Python"
proxy_addr="182.88.214.145:8123"
for i in range(1, 5):
    key=urllib.request.quote(key)
    thispageurl='https://weixin.sogou.com/weixin?query='+key+'&_sug_type_=&sut=2345&lkt=7%2C1536736051129%2C1536736053327&s_from=input&_sug_=y&type=2&sst0=1536736053539&page='+str(i)+'&ie=utf8&w=01019900&dr=1'
    thispagedata=use_proxy(proxy_addr,thispageurl)
    # print(len(thispagedata))
    pat=r'<a target="_blank" href="(.*?)"'
    rs1=re.compile(pat).findall(thispagedata)
    if len(rs1)==0:
        print("此次("+str(i)+"页)没成功")
        continue
    for j in range(0,len(rs1)):
        thisurl=rs1[j]
        #http://mp.weixin.qq.com/s?src=11&amp;timestamp=1536736085&amp;ver=1117&amp;signature=uPU-E3cysQcIULZ4R6llc9nFrPWek56Wi0mR7Qmp8INDRL9QutzblK525rpvzn0iLcCt*kjTlRicgx*t2Zvj*WNTdaGB9VTNxcvBi4q1QZqQzGyAF9t0hvcpPPBU7P8T&amp;new=1
        thisurl=thisurl.replace("amp;","")
        #file=os.path.join(r"F:\Python\爬虫与数据分析\day04\千图网图片", str(i)+str(j)+".jpg")
        file=os.path.join('F:/Python/爬虫与数据分析/day05/微信文章', str(i)+str(j)+".html")
        thisdata=use_proxy(proxy_addr,thisurl)
        try:
            with open(file,"w",encoding="utf-8") as f:
                f.write(thisdata)
            f.close()
            print("第"+str(i)+"页第"+str(j+1)+"篇文章爬取成功")
        except Exception as e:
            print(e)
            print("第"+str(i)+"页第"+str(j+1)+"篇文章爬取失败")

























