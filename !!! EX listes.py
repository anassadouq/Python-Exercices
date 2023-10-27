#1
l=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(l)):
    l[i]=l[i]+1
print(l)
#2
l.append(11)
print(l)
#3
l.append(12)
l.append(13)
print(l)
#4
print(l[0])
print(l[0:2])
print(l[-1])
print(l[-2:])
#5
limp=[]
lp=[]
for i in range(len(l)):
    if l[i]%2==0:
       lp.append(l[i])
    else:
         limp.append(l[i])
#6
l.insert(4,'3.5')
print(l)
#7
del l[4]
print(l)

