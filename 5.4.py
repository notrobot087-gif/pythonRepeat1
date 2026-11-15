num=[]

a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    num.append(r)
num.insert(2,0)
print(num)
num.remove(0)
print(num)