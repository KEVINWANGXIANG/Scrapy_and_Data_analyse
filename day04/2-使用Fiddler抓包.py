'''
https://rate.tmall.com/list_detail_rate.htm?itemId=552403179992&spuId=853636606&
sellerId=1621790841&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=
&ua=098%23E1hvs9vEvbQvUvCkvvvvvjiPPsdO0jimPFq9tjD2PmPpAjiWnLdv6jEVR2MpAj3W3QhvChCC
vvvtvpvhphvvvvhCvvXvppvvvvvEvpCWpZP1v8RAnhhAcUmD5dUfb363D76Od5Yjw62vTCKwayB%2BVd0D
W3CQoAnmsXZpVcIUExjxALwpEcttEPoxdXIankx%2F6jZ7%2B3%2BKjomUaOyCvvXmp99hVteivpvUphvhD7
pczcmtvpvIphvvvvvvphCvpCBXvvCmNhCvHHyvvhn2phvZ7pvvpiivpCBXvvCme9GCvvpvvPMMiQhvChCvCC
p%3D&needFold=0&_ksTS=1536661946082_1758&callback=jsonp1759
'''
import re,os
import urllib.request

for i in range(1, 6):
    reviewPage="https://rate.tmall.com/list_detail_rate.htm?itemId=552403179992&spuId=853636606&sellerId=1621790841&order=3&currentPage="+str(i)+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvs9vEvbQvUvCkvvvvvjiPPsdO0jimPFq9tjD2PmPpAjiWnLdv6jEVR2MpAj3W3QhvChCCvvvtvpvhphvvvvhCvvXvppvvvvvEvpCWpZP1v8RAnhhAcUmD5dUfb363D76Od5Yjw62vTCKwayB%2BVd0DW3CQoAnmsXZpVcIUExjxALwpEcttEPoxdXIankx%2F6jZ7%2B3%2BKjomUaOyCvvXmp99hVteivpvUphvhD7pczcmtvpvIphvvvvvvphCvpCBXvvCmNhCvHHyvvhn2phvZ7pvvpiivpCBXvvCme9GCvvpvvPMMiQhvChCvCCp%3D&needFold=0&_ksTS=1536661946082_1758&callback=jsonp1759"
    data=urllib.request.urlopen(reviewPage).read().decode("utf-8","ignore")
    print(len(data))
    pat=r'"rateContent":"(.*?)",'
    reviewList=re.compile(pat).findall(data)
    for review in reviewList:
        with open(r'F:\Python\爬虫与数据分析\day04\file1.txt', "a", encoding="utf-8") as f:
            f.write(review+"\n")
























