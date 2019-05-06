
import urllib.request

'''
触发URLError的几种情况：
1.连不上服务器
2.远程的URL不存在
3.本地没有网络
4.触发了HTTPError
'''

import urllib.error

try:
    urllib.request.urlopen("https://www.csdn.net/")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)


















