M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

min_val, max_val = matrix[0][0], matrix[0][0]
min_col, max_col = 0, 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_col = j
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_col = j

if min_col != max_col:
    for i in range(M):
        matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

print("Преобразованная матрица:")
for row in matrix:
    print(*row)
