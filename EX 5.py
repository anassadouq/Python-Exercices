def cubique(n):
    s=0
    P=n
    for i in range(1,4):
        r=n%10
        s=s+r**3
        n=n//10
    if(P==s):
        return 1
    else:
        return 0
N=int(input("vueillez donner une valeur"))
while N<100 or N>999:
    N=int(input("vueillez donner une valeur"))
R=cubique(N)
if (R==1):
   print("le nombre est cubique")
else:
    print("le nombre est non cubique")

