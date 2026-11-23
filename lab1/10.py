import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

a = get_distance(x1, y1, x2, y2)
b = get_distance(x2, y2, x3, y3)
c = get_distance(x3, y3, x1, y1)


perimeter = a + b + c
p = perimeter / 2

# Площадь по формуле Герона
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Периметр треугольника: {perimeter}")
print(f"Площадь треугольника: {area}")
