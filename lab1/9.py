x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

width = abs(x2 - x1)
height = abs(y2 - y1)

perimeter = 2 * (width + height)
area = width * height

print(f"Периметр прямоугольника: {perimeter}")
print(f"Площадь прямоугольника: {area}")
