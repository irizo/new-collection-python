# new-collection-python
I started learning python two days ago, I found it so attracted to me, so I started writing my first project, call it prjno1. It's collecting news form diffierent webs together, I pull this up to let your guys to pull your ideas into this, lets make it better. v0.1--collect cnbeta.com ithome.com without input

here is the lastest version


import requests
from bs4 import BeautifulSoup
url = "http://www.cnbeta.com/"
data1 = requests.get(url).content
data1 = str(data1,"utf-8")
soup1 = BeautifulSoup(data1,'lxml')
#print(soup)
list1 = soup1.select("dl > dt > a")
#print(list)
out1 = ['']
for i in list1:
    url = i.get("href")
    title = i.text
    out1.append( url )
    out1.append( title )
url = "https://m.ithome.com/"
data = requests.get(url).content
data = str(data,"utf-8")
#print(data)
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
doc = open('test.txt','w')
for z in range(20):
   r = ( 2 * z ) + 1 
   p = r + 1 
   tx.append( r ) 
   tx.append( out1[p] ) 
   tx.append( out1[r] ) 
   tx.append( p ) 
   tx.append( out[p] ) 
   tx.append( out[r] )
h = 0
#for i in range(120):
  #h = tx[i]
print('tx',file=doc)
print(tx)
doc.close()
