A = float(input("Введите координату A: "))
B = float(input("Введите координату B: "))
C = float(input("Введите координату C: "))

AC = abs(C - A)
BC = abs(B - C)
product = AC * BC

print(f"Произведение длин AC и BC: {product}")
