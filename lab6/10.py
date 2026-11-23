M = int(input("Введите порядок квадратной матрицы M: "))

print("Введите элементы матрицы построчно через пробел:")
A = [list(map(float, input().split())) for _ in range(M)]

print("Суммы диагоналей, параллельных главной:")
for k in range(-(M - 1), M):
    diag_sum = 0
    for i in range(M):
        j = i - k
        if 0 <= j < M:
            diag_sum += A[i][j]
    print(f"Диагональ (i - j = {k}): {diag_sum}")
