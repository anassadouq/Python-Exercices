N=int(input("donner une valeur"))
while N==1:
    N = int(input("donner une valeur"))
c=0
for i in range(1,N+1):
    if N%i==0:
        c=c+1

if(c==2):
    print("ce nombre est premier")
else:
    print("ce nombre n'est pas premier")


