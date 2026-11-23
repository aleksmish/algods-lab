M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

matrix.sort(key=lambda row: row[0])

print("Упорядоченная матрица:")
for row in matrix:
    print(*row)
