import math

deg = float(input("Введите угол в градусах: "))
rad = math.radians(deg)

i = math.sin(rad)**2 + math.cos(rad)**2
print(i)