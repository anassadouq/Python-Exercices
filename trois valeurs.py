A = int(input ("veuillez entrer la valeur de A:"))
B = int(input ("vueillez entrer la valeur de B:"))
C = int (input("veuillez entrez la valeur de C:"))
if (A>B and A>C) :
    max=A
elif(B>A and B>C) :
    max=B
else :
    max=C
print("Le maximum est ",max)
