#nombre **2
list1=[]
for x in range(5):
    list1.append(x**2)
print(list1)
list1=[x**2 for x in range(5)]
print(list1)
#les tuples non modifiables
tupl=(1,5,6,3,2,4)
print(max(tupl))
print(min(tupl))