def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c
a1=int(input("a"))
b1=int(input("b"))
c1=int(input("c"))
print(min_of_three(a1,b1,c1))