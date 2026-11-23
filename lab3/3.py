n = int(input("Введите N (> 0): "))
total = 0
for i in range(1, n + 1):
    total += 2 * i - 1
    print(f"Шаг {i}: сумма = {total}")
