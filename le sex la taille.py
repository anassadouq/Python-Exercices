S=input("donner le sex")
P=float(input("donner le poids"))
T=float(input("donner la taille"))
if (S=='H') :
    PI=(T-100)-(T-150)/4
elif (S=='F') :
    PI=(T-100)-(T-120)/4
print("le poids ideal est",PI)
T=T/100
BMI =P/(T**2)
print("indication d'obisite est",BMI)
if(BMI<=27):
    print("vous etes normal")
elif (BMI<32):
    print("vous etes obese")
else:
    print("vous etes malade")
