M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

min_prod = float('inf')
min_col = -1

for j in range(N):
    prod = 1
    for i in range(M):
        prod *= matrix[i][j]
    if prod < min_prod:
        min_prod = prod
        min_col = j + 1

print(f"Номер столбца с наименьшим произведением: {min_col}")
print(f"Значение наименьшего произведения: {min_prod}")
