def fct(n):
    if n==1 or n==2:
        return 1
    else:
        return (fct(n-1) +fct(n-2))
N=int(input("vueillez donner une valeur"))
R=fct(N)
print("le resulat est",R)
