
#http://www.58pic.com/piccate/3-8-293.html
#http://www.58pic.com/piccate/3-8-293-default-0_2_0_0_default_0-2.html
#http://www.58pic.com/piccate/3-8-293-default-0_2_0_0_default_0-3.html

'''

http://pic.qiantucdn.com/58pic/28/85/91/53m58PICA223bb76deb1B_PIC2018.jpg!qtwebp324
http://pic.qiantucdn.com/58pic/28/85/91/53m58PICA223bb76deb1B_PIC2018.jpg!
/fw/1024/watermark/url/L2ltYWdlcy93YXRlcm1hcmsvZGF0dS5wbmc=/repeat/true/crop/0x1024a0a0




http://pic.qiantucdn.com/58pic/32/26/35/97t58PIC2K2rcc4u8jWNh_PIC2018.jpg!qtwebp324
http://pic.qiantucdn.com/58pic/32/26/35/97t58PIC2K2rcc4u8jWNh_PIC2018.jpg!
/fw/1024/watermark/url/L2ltYWdlcy93YXRlcm1hcmsvZGF0dS5wbmc=/repeat/true/crop/0x1024a0a0
'''

import re,os
import urllib.request


for i in range(1,5):
    pageurl="http://www.58pic.com/piccate/3-8-293-default-0_2_0_0_default_0-"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    # with open(r"F:\Python\爬虫与数据分析\day04\file1.html", "w",encoding="utf-8") as f:
    #     f.write(data)
    pat=r'<div class="card-tag-business a8"></div></div><img  src="(.*?)qt324"'
    imgList=re.compile(pat).findall(data)
    imgList=list(set(imgList))
    # print(len(imgList))
    # print(imgList)
    for j in range(0,len(imgList)):
        try:
            thisimg=imgList[j]+"/fw/1024/watermark/url/L2ltYWdlcy93YXRlcm1hcmsvZGF0dS5wbmc=/repeat/true/crop/0x1024a0a0"
            file=os.path.join(r"F:\Python\爬虫与数据分析\day04\千图网图片", str(i)+str(j)+".jpg")
            urllib.request.urlretrieve(thisimg,filename=file)
            print("第%d页,第%d张爬取成功" %(i, j+1))
        except Exception as e:
            print("第%d页,第%d张爬取失败" %(i, j+1))





















