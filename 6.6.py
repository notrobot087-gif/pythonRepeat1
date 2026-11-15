num=[]

a=int(input("quantity"))
k=0
for i in range(0,a):
    r=int(input())
    k+=r
    num.append(r)
list1=[x for x in num if x<k/a]
print(list1)
    