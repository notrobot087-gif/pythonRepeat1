a=str(input("Text:    "))
b=int(input("quantity:    "))
banned_words=[]
for i in range(b):
    banned_words.append(str(input()))
for word in banned_words:
    a=a.replace(word,"*")

print(a)
