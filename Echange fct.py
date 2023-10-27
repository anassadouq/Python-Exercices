def echange(A,B):
    A,B=B,A
    return A,B
X=int(input("vueillez donner une valeur"))
Y=int(input("vueillez donner une valeur"))
X,Y=echange(X,Y)
print("la nouvelle valeur de X est", X)
print("la nouvelle valeur de Y est", Y)



