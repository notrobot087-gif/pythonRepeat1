def power_count(base,exponent):
    i=0
    while exponent>1:
        exponent=exponent/base
        i+=1
    return i
a=int(input("base"))
exponent=int(input("exponent"))
print(power_count(a,exponent))