import re

pat="yue"
str="http://yum.iqianyyue.com"
rst1=re.search(pat, str)
print(rst1)
string2="acbsdc gsc"
rst2=re.search(pat, string2)
print(rst2)
pat2="\n"
string3='''cdsbhcjdsh
dsvvdfvdfv'''
rst3=re.search(pat2, string3)
print(rst3)
print(re.search(r'\w', "sc12cs12dcs"))

pat3=r"\w\dpython\w"
rst4=re.search(pat3, "11python_")
print(rst4)

pat4=r"pyth[jsz]n"
print(re.search(pat4,"111pythznsdcd"))

pat=".python..."
string="cvdfvpythoncsdcsd"
rst=re.search(pat,string)
print(rst)

pat=r"python|php"
string="abcdphp5151pythonvddf"
rst=re.search(pat, string)
print(rst)

pat1=r"python"
pat2=r"python"
string="csnjcsdjPythoncdsjhjhvdf"
rst=re.search(pat1, string)
print(rst)
rst=re.search(pat2, string, re.I)
print(rst)

pat1=r"p.*y"
pat2=r"p.*?y"
str="abcdscsdpythonpycdnjc"
rst=re.search(pat1,str)
print(rst)
rst=re.search(pat2,str)
print(rst)
rst=re.match(pat1,str)
print(rst)

str="pchdsdhvbgvdbdcdhy"
pat1=r"p.*y"
print(re.match(pat1,str))

pat=r"p.*?y"
str="cdpcbdshydbampbffyry"
print(re.search(pat,str))
print(re.findall(pat,str))

pat=r"[a-zA-Z]+://[^\s]*[(.com)|(.cn)]"
str='<a href="http://www.baidu.com"></a>'
rst2=re.compile(pat).findall(str)
print(rst2)











































