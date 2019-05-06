
import urllib.request
import re

# try:
#     file=urllib.request.urlopen("http://www.baidu.com",timeout=0.1)
# except:
#     print("超时")

for i in range(0, 100):
    try:
        file=urllib.request.urlopen("http://www.baidu.com", timeout=0.1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常:"+str(e))

