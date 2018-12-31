# -*- coding:utf-8 -*-
import requests
import os

url='http://photo1.cazdiy.com/images/20/2018/08/k20siV1SZi00Si9V000IMSYyC9S9Vy.jpg'
root='d://pic//'
path=root+'10.jpg'

try:
   if not os.path.exists(root):
      os.mkdir(root)
   if not os.path.exists(path):
      r=requests.get(url)
      with open(path,'wb') as f:
         f.write(r.content)
         print('写入成功过')
         f.close
   else:
      print('failure')
except:
   print('写入失败')
