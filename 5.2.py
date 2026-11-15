numbers=[]

a=int(input("quantity"))
for i in range(0,a):
    r=int(input())
    numbers.append(r)

negative_numbers = []

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < 0:
        a = numbers.pop(i)
        negative_numbers.append(a)

# Так как мы удаляли с конца, порядок в negative_numbers получится обратным. Развернем его:
negative_numbers.reverse()

print(numbers)
print(negative_numbers)