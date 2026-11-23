n = int(input("Введите N (> 0): "))
res = 1.0
for i in range(1, n + 1):
    res *= 1 + i / 10
print("Произведение:", res)
