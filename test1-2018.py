#s1='k:1|k1:2|k2:3|k3:4'
#d1={'k':1,'k1':2,'k2':3,"k3":4}
s1=a.split('|')
s1=[str(x.split(':')[0]),int((x.split(":")[1])) for x in s1]
d1=s1.replace(",",":").replace("(","").replace(")","").replace("[","{").replace("]","}")
d1=eval(d1)
print(d1)
