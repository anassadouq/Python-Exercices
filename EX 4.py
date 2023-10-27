def puissance(p,n):
    S=0
    for i in range(1,n+1):
        S=S+i**p
    return S
X=int(input("donner une valeur"))
Y=int(input("donner une valeur"))
R=puissance(X,Y)
print("la somme des puissances est",R)
