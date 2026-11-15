num=[]

a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    num.append(r)
for i in range(0,a):
    if(num[i]%7==0):
        print(i)
        break
