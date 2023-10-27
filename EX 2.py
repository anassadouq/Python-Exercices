def pgcd(a,b):
    if a<b:
        mini=a
    else:
        mini=b
    for i in range (1,mini+1):
        if (a%i==0) and (b%i==0):
            pgcd=i
    return pgcd
x=int(input("donner un valeur : "))
y=int(input("donner un valeur : "))
R=pgcd(x,y)
print("le pgcd est : ",R)