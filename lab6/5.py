M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите целочисленную матрицу построчно через пробел:")
matrix = [list(map(int, input().split())) for _ in range(M)]

result_col = 0

for j in range(N):
    if all(matrix[i][j] % 2 != 0 for i in range(M)):
        result_col = j + 1
        break

print(f"Результат: {result_col}")
