M = int(input("Введите четное количество строк M: "))
N = int(input("Введите четное количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

half_M = M // 2
half_N = N // 2

for i in range(half_M):
    for j in range(half_N):
        matrix[i][j], matrix[i + half_M][j + half_N] = (
            matrix[i + half_M][j + half_N],
            matrix[i][j]
        )

print("Преобразованная матрица:")
for row in matrix:
    print(*row)
