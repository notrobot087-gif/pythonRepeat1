x = float(input("Введитe x: "))
y = float(input("Введите y: "))
R = float(input("Введите R: "))

if x**2 + y**2 <= R**2:
    print("В круге.")
else:
    print("Вне круга.")