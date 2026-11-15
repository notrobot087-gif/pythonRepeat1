a=str(input("String:    "))
if a.isdigit():
    k=sum(int(char) for char in a)
    print(k)
else:
    print("it has letters")