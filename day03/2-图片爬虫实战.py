
import urllib.request
import re,os

'''
https://s.taobao.com/list?spm=a217f.8051907.312344.6.60623308JO2VNp&q=%E6%AF%9B%E8%A1%A3
&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=0

"https://s.taobao.com/list?spm=a217f.8051907.312344.6.60623308JO2VNp&q=%E6%AF%9B%E8%A1%A3
&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=60"

https://s.taobao.com/list?spm=a217f.8051907.312344.6.60623308JO2VNp&q=%E6%AF%9B%E8%A1%A3
&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s=120

'''
keyname="连衣裙"
key=urllib.request.quote(keyname)
for i in range(0,10):
    url="https://s.taobao.com/list?spm=a217f.8051907.312344.6.60623308JO2VNp&q="+key+"&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s="+str(i*60)
    data=urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    pat=r'"picUrl":"//(.*?)",'
    imageList=re.compile(pat).findall(data)
    imageList=list(set(imageList))
    for j in range(0,len(imageList)):
        thisimage=imageList[j]
        thisimgurl="http://"+thisimage
        # file=r"F:\Python\爬虫与数据分析\day03\爬取淘宝图片"+str(i)+str(j)+".jpg"
        file=os.path.join(r"F:\Python\爬虫与数据分析\day03\爬取淘宝图片",str(i)+str(j)+".jpg")
        urllib.request.urlretrieve(thisimgurl,filename=file)

    # print(imageUrl)
# print(len(imageUrl))

# print(len(data))
'''
num=1
for imageUrl in imageUrls:
    path=os.path.join(toPath,str(num)+".jpg")
    num+=1
    #把图片下载到本地存储
    urllib.request.urlretrieve("http://"+imageUrl,filename=path)
'''

#https://g-search2.alicdn.com/img/bao/uploaded/i4/i1/1095921593/O1CN011NddNvKR4aWhTML_!!1095921593.jpg_230x230.jpg_.webp

#http://www.58pic.com/


#http://www.58pic.com/newpic/32191944.html
#http://www.58pic.com/newpic/28919092.html
#http://www.58pic.com/newpic/28865322.html













