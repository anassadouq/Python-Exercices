#question 1
D={'nom':'depuis','prenom':'jacke','age':30}
D["prenom"]="jackes"
print(D)
#question 2
for cles in D.keys():
    print(cles,"-->",D[cles])
#question 3
for val in D.values():
    print(val)
#question 4
for cles , val in D.items():
    print(cles,"/",val)
#question 5
for val in D.values():
    print(val,end=" ")
print("ans")