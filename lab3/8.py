n = int(input("Введите N (> 1): "))
k = 0
total = 0
while total < n:
    k += 1
    total += k
print(f"K = {k}, сумма = {total}")
