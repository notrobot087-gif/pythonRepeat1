words=[]

a=int(input("quantity"))
for i in range(0,a):
    r=str(input())
    words.append(r)
length=[len(word) for word in words]
print(length)
