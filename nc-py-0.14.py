#coding=utf-8
#!/usr/bin/python
#-*-coding:utf-8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import json
import requests
from bs4 import BeautifulSoup
url = "http://www.cnbeta.com/"
data1 = requests.get(url).content
data1 = str(data1,"utf-8")
soup1 = BeautifulSoup(data1,'lxml')
print(soup1)
list1 = soup1.select("dl > dt > a")
#print(list1)
out1 = ['']
for i in list1:
    url = i.get("href")
    title = i.text
    out1.append( url )
    out1.append( title )


url = "https://m.ithome.com/"
data = requests.get(url).content
data = str(data,"utf-8")
print(data)
soup = BeautifulSoup(data,'lxml')
#print(soup)
#list = soup.select("dl > dt > a")
list = soup.select("a[role=option]")
out = ['']
for i in list:
    url = i.get("href")
    title = i.text
    out.append( url )
    out.append( title )
tx = ['']
r = 0
p = 0

doc = open('test1.txt','w')

for z in range(20):
   r = ( 2 * z ) + 1 
   p = r + 1 
   tx.append( r ) 
   tx.append( out1[p] ) 
   tx.append( out1[r] ) 
   tx.append( p ) 
   tx.append( out[p] ) 
   tx.append( out[r] )

#txc = str(tx).replace('u\'','\'')
#txc.decode("unicode-escape")

h = 0
#for i in range(120):
  #h = tx[i]
#tx = str(tx)

for h in range(120):

    doc.write(str(tx[h]) + "\n")
#doc.write(str(txc)+"\n")

doc.close()


GEN_HTML = "demo_21.html"  #命名生成的html

f = open(GEN_HTML,'w')
message = """
<html>
<meta charset="utf-8">
<head></head>
<body>
</body>
</html>"""

f.write(message)
k = 0
for k in range(1,120):   
    if k%3==0:
        f.write("<p><a href=%s></p>" % tx[k])
        f.write("<p>%s</p><a>" % tx[k])
        f.write("<br>")
    else:
        f.write("<p>%s</p>" % tx[k])


f.close()



#print('tx',file=doc)
print(tx)
