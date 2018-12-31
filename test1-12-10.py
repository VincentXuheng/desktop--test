import os
import xlsxwriter
import re
import tkinter as tk
import platform
import logging.handlers
window = tk.Tk()
window.geometry('800x600')
var1=[]
var2=[]
var3=[]
var4=[]
def calc(s,num,n):
    locals()['gd%s'%n]=[]
    for q in range(int(num)):
        r=re.findall(r'[0-9]',str(s))
        lst=[]
        for i in range(len(r)):
            lst.append(int(r[i]))
        qr=10-(sum(lst[::2])*3+sum(lst[1::2]))%10
        if qr==10:
            qr=0
        tiaoma=int(str(s)+str(qr))
        locals()['gd%s'%n].append(tiaoma)
        s=s+1
    return(locals()['gd%s'%n])
def next_to():
    global var1
    global var2
    global var3
    global var4
    var1.append(t1.get())
    var2.append(t2.get())
    var3.append(t3.get())
    var4.append(t4.get())
    tx.insert('insert',"订单{0}：， 数量为：{1} ，起条码为：{2} ， 终条码为：{3}\n".format(var1[-1],var4[-1],var2[-1],var3[-1]))
    t1.delete(0,50)
    t2.delete(0,50)
    t3.delete(0,50)
    t4.delete(0,50)

def start_calc():
    nn=len(var4)
    for i in range(nn):
        locals()['god%s'%i]=calc(s=int(var2[i]),num=var4[i],n=i)
    workbook=xlsxwriter.Workbook(u'f:\资产条码.xlsx')
    title=[u'资产条码',u'取45']
    for m in range(nn):
        locals()['worksheet%s'%m]=workbook.add_worksheet(str(var1[m]))
        locals()['worksheet%s'%m].write_row('A1',title)
        for q in range(len(locals()['god%s'%m])-1):
            num0 = str(q+2)
            row = 'A' + num0
            data = [str(locals()['god%s'%m][q]),]
            locals()['worksheet%s'%m].write_row(row, data)
    workbook.close()

tk.Label(window, text="订单号：").place(x=20, y=10)
t1=tk.Entry(window,show=None,width=23)
t1.place(x=80,y=10)
tk.Label(window, text="起条码：").place(x=20, y=40)
t2=tk.Entry(window,show=None,width=23)
t2.place(x=80,y=40)
tk.Label(window, text="终条码：").place(x=20, y=70)
t3=tk.Entry(window,show=None,width=23)
t3.place(x=80,y=70)
tk.Label(window, text="数量：").place(x=20, y=100)
t4=tk.Entry(window,show=None,width=23)
t4.place(x=80,y=100)
tk.Button(window,text="下一订单",command=next_to).place(x=20,y=130)
tk.Button(window,text="开始计算",command=start_calc).place(x=200,y=130)
tx=tk.Text(window,width=500)
tx.place(x=20,y=200)
window.mainloop()



















    
