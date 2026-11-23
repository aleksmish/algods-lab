a = float(input("Введите A: "))
n = int(input("Введите N (> 0): "))
total = 1.0
term = 1.0
for _ in range(n):
    term *= a
    total += term
print("Сумма:", total)
