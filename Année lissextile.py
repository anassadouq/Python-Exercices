def jours(N):
    while N>=2021:
        print("donner une autre valeur")
    if N==366 :
        print("l'année est lissextile")
    else:
        print("l'année n'est pas lissextile")
    return N
X=int(input("vueillez donner une valeur"))
R=jours(X)
print("l'année est",R)