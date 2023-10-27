n=int(input("vueillez donner une valeur"))
t=[0]*n
for i in range(n):
    t[i]=int(input("vueillez donner une valeur"))
print(t)
max=t[0]
for i in range(n):
   if t[i]>max:
        max=t[i]
print("le maximum est",max)
       #position max
n=int(input("vueillez donner une valeur"))
t=[0]*n
for i in range(n):
    t[i]=int(input("vueillez donner une valeur"))
print(t)
pmax=0
for i in range(n):
    if t[pmax]<t[i]:
        pmax=i
print("la position max est",pmax)
print("le maximum est",t[pmax])