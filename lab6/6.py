M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

for row in matrix:
    min_idx = row.index(min(row))
    max_idx = row.index(max(row))
    row[min_idx], row[max_idx] = row[max_idx], row[min_idx]

print("Преобразованная матрица:")
for row in matrix:
    print(*row)
