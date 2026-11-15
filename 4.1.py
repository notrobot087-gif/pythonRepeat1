def is_prime(n):
    k=0
    for i in range(2,n):
        if n % i == 0:
            k+=1
    if k==1:
        return True
    else:
        return False

a=int(input("Введите число "))
print(is_prime(a))