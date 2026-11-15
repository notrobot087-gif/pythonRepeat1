a=str(input("Text:    "))
words=a.split()
A=[word.capitalize() for word in words]
sentence=" ".join(A)
print(sentence)