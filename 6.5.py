listr=[]

a=int(input("quantity"))
for i in range(0,a):
    r=str(input())
    listr.append(r)
for i,word in enumerate(listr):
    if i%2==0:
        print(i,word)

