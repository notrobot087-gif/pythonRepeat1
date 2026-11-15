words=[]
a=int(input("quantity"))
for i in range(a):
    words.append(str(input()))

worda=[word for word in words if word.startswith(('А','а'))]
print(worda)
