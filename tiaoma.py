# -*- coding:utf-8 -*-

import re
import csv
s=int(input("请输入起条码："))
s1=int(input("请输入终条码："))
num=s1-s+1
god=[]
for q in range(num):
   r=re.findall(r'[0-9]',str(s))
   list=[]
   for i in range(len(r)):
       list.append(int(r[i]))
   qr=10-(sum(list[::2])*3+sum(list[1::2]))%10
   if qr==10:
      qr=0
   tiaoma=int(str(s)+str(qr))
   god.append(tiaoma)
   s=s+1
for i in range(len(god)):
   print(god[i])
with open('D:\\pic\\2.txt','a') as f:
   for i in range(len(god)):
      f.write(str(god[i]))
with open('D:\\pic\\1.csv','a') as csvfile:
        write=csv.writer(csvfile)
        write.writerows(str(god))
