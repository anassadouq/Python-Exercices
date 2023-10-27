def symet (li,m):
    for i in range(m):
        for j in range(m):
            if (i!=j and li[i][j]!=li[j][i]):
                return 0
    return 1
n=int(input("vueillez donner la taille"))
liste=[ [int(input("donner une valeur"))for j in range(n)] for i in range(n)]
R=symet(liste,n)
if R==1:
    print("matrice symetrique")
else:
    print("matrice n'est pas symetrique")