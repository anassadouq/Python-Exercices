S=0
for i in range(1,9):
    print("donner une valeur")
    N=int(input())
    if N<0:
       break
    S=S+N
print("la somme est",S)