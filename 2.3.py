N = int(input("Введите число N: "))
res = 1

for i in range(1, N + 1):
    res *= i

print(res)