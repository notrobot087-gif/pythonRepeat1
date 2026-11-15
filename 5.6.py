num = []
a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    num.append(r)
num.reverse()
print(num[0:a:2])