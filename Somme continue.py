S=0
for i in range(1,9):
    print("vueillez N",i,":",)
    N=int(input())
    if N<0:
        continue
    S=S+N
print("la somme est",S)
