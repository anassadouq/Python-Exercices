def multiplication(N):
    for i in range(0,11):
        M=N*i
        print(i,"*",N,"=",M)
    return M
X=int(input("vueillez donner une valeur"))
D=multiplication(X)
print("la multiplication est",D)