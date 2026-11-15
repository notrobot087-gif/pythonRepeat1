num=[]
n=[]

a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    num.append(r)
n.append(num[0])
for i in range(a-2,0,-1):
    n.append(num[i])
n.append(num[a-1])
print(n)
