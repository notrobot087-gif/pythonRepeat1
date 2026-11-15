num=[]
a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    num.append(r)
num1=[]
l2=len(num)//2
num1=num[l2:]+num[:l2]
print(num1)