a=int(input("Enter 3-digit number :  |   "))
a1=a//100
a2=(a//10)%10
a3=a%10
b=a1+a2+a3
if b%2==0:
    print("The sum of number is even")
elif b%2!=0:
    print("The sum of number is odd")


