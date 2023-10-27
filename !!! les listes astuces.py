#1 créer une liste
couleur=["rojo","azul","verde",]
print(couleur)
#2 présenter un element
print(couleur[1])
#3 présenter le dernier element
print(couleur[2:])
#4 modifier un element
couleur[1]="blue"
print(couleur)
#5 ajouter des elements
couleur.insert(3,"sombrero")
print(couleur)
#6 pour afficher les derniers valeurs
print(couleur[2:4])
#7 sombrero and verde to gracis and adios
couleur[4:2]=["gracias","adios"]
print(couleur)
#8 ajouter des elements a la fin
couleur.append("por favor")
couleur.append("mucho gusto")
print(couleur)
#9 supprimer une valeur
del couleur[1] #ou couleur.pop[1]
print(couleur)
#10 pour trier
mylist=[2,5,8,6,3,]
mylist.sort()
print(mylist)
#11 liste to chaine
liste=['b','o','n','j','o','u','r']
chaine="_".join(liste)
print(chaine)
#12 chaine to liste
chaine="b:o:n:j:o:u:r"
liste=chaine.split(":")
print(liste)