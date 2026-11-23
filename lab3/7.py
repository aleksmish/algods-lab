a = float(input("Введите длину A: "))
b = float(input("Введите длину B (A > B): "))
while a >= b:
    a -= b
print("Длина незанятой части:", a)
