N=int(input("donner une valeur"))
while(N<100 or N>999):
    N = int(input("donner une valeur"))
S=0
P=N
for i in range(1,4):
    R=N%10
    S=S+R**3
    N=N//10
if (P==S):
    print("cubique")
else:
    print("non cubique")
