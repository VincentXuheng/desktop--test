# -*- coding:utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup
import csv

url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
ulist=[]
num=int(input('请输入需要多少：'))

r=requests.get(url,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding
html=r.text
soup=BeautifulSoup(html,'html.parser')
for tr in soup.find('tbody').children:
    if isinstance(tr,bs4.element.Tag):
        tds=tr('td')
        ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string,tds[5].string])

print("{:^10}\t{:^6}\t{:^10}".format("排名",'学校名称',"地区"))
for i in range(num):
    u=ulist[i]
    print('{:^10}\t{:<15}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'.format(u[0],u[1],u[2],u[3],u[4],u[5]))
    with open('D:\\pic\\2.txt','a') as f:
        f.writelines('{:^10}\t{:^15}\t{:^10}'.format(u[0],u[1],u[2])+'\n')

       
    

