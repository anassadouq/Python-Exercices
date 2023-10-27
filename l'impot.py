S = input("vueillez donner le sex")
A = int(input("vueillez donner l'age"))
if (S=="H") :
    if(A>=20) :
      print("paient l'impot")
    elif(A<20) :
      print("ne paient pas l'impot")
if (S=="F") :
    if(A>=18 and A<=35) :
      print("paient l'impot")
    else :
      print("ne paient pas l'impot")

