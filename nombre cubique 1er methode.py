N=int(input("donner une valeur"))
while(N<100 or N>999):
    N = int(input("donner une valeur"))
A=N//100
B=N%100
C=B//10
R=R%10
S=A**3+B**3+C**3
if S==N:
  print("le nombre est cubique")
else:
    print("le nombre n'est pas cubique")



