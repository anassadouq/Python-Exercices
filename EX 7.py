def fact(n):
    if n==0 or n==1:
        return 1 #role#
    else:
        return n*fact(n-1)
def somme(n):
    S=0
    for i in range(1,n+1):
        S=S+1/fact(n)
        return S
N=int(input("donner une valeur"))
while N%2==0 or N<5:
    N=int(input("donner une valeur"))
R=somme(N)
print("la somme est",R)

