def chiffres (n):
  c=0
  while n!=0:
    n = n // 10
    c=c+1
  return c

x=int(input("donner une valeur"))
R=chiffres(x)
print("les chiffres sont",R)