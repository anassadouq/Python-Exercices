A=input("vueillez entrer la valeur de A")
B=input("vueillez entrer la valeur de B")
if ((A>0 and B>0) or (A<0 and B<0)):
    print("le signe de A et B est positif")
elif ((A>0 and B<0) or (A<0 and B>0)):
    print("le signe de A et B est negatif")
if (A>0 and B<0) :
    print("le signe de A et B est negatif")
elif (A<0 and B>0) :
    print("le signe de A et B est positif")
else :
    print("le signe est nul")
