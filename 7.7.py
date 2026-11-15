a=str(input("Text:    "))
cleantext=a.strip().lower().split()
for word in cleantext:
    print(word)