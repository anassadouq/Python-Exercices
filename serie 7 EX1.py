def max(A,B):
    if A>B:
        max=A
    else:
        max=B
    return max
x=int(input("doner une valeur"))
y=int(input("donner une valeur"))
R=max(x,y)
print("le maximum est",R)
