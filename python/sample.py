
from bs4 import BeautifulSoup as bs
import requests
v="INFY"
link="https://www.google.com/finance/quote/"+v+":NSE"
page=requests.get(link)
soup=bs(page.content,'lxml')
ltp=soup.find('div',class_="YMlKec fxKbKc").text
pre=soup.find_all('div',class_="M2CUtd")
head=soup.find('h1',class_="kHAtIb").text
time=soup.find('div',class_="ygUjEc")
prev=pre[0].text
dayL=pre[1].text.partition('-')[0]
dayH=pre[1].text.partition('-')[2]
yL=pre[2].text.partition('-')[0]
yH=pre[2].text.partition('-')[2]
cap=pre[3].text
PE=pre[4].text
div=pre[5].text
iltp=float(ltp.replace('\u20B9','').replace(',',''))
ipre=float(prev.replace('\u20B9','').replace(',',''))
res=round((iltp-ipre),2)
text=str(res)+" Today"
print(time)