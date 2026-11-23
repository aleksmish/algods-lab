A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))

AC = abs(C - A)
BC = abs(C - B)
total = AC + BC

print("Длина AC =", AC)
print("Длина BC =", BC)
print("Сумма длин =", total)
