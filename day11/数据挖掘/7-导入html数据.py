
import pandas
#读取网页中的表格

i=pandas.read_html('https://www.douban.com/photos/album/1657236035/')
print(i)