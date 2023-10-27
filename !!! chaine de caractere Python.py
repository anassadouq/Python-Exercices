ch="bonjourMrADIL"
caractere=min(ch)
print(caractere)
caractere2=max(ch)
print(caractere2)
pos=ch.index('M')
print("la position est",pos)
NB=ch.count('o')
print("le nombre d'occurence est",NB)
chaine=ch.capitalize()
print(chaine)
bol=ch.endswith("IL")
if bol==True:
    print("la chaine se termine par IL")
else:
    print("la chaine ne termine pas par IL")
bol=ch.startswith("bo")
if bol==True:
    print("chaine commence par bo")
else:
    print("la chaine ne commznce pas par bo")
entier=ch.find("on")  #entier=ch.find('o',3)
if entier==-1:        #if entier==-1:
    print("la solution n'existe pas") #print("la solution n'existe pas")
else:                 #else:
    print("la position est",entier) #print("la position est",entier)
entier=ch.rfind("o")
if entier==-1:
    print("la solution n'existe pas")
else:
    print("la position est",entier)

