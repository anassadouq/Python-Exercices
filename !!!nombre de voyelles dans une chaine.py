def voyelles(ch):
    c=0
    for x in ch:
        x=x.lower()
        if x=='a'or x=='e' or x=='i' or x=='u' or x=='y' or x=='o':
           c=c+1
    return c
chaine=input("vueillez donner une valeur")
A=voyelles(chaine)
print("le nombre des voyelles est",A)