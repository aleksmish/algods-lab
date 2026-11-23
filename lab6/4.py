M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))

print("Введите элементы матрицы построчно через пробел:")
matrix = [list(map(float, input().split())) for _ in range(M)]

for j in range(N):
    col = [matrix[i][j] for i in range(M)]
    avg = sum(col) / M
    count = sum(1 for x in col if x > avg)
    print(f"Столбец {j + 1}: элементов больше среднего ({avg:.2f}) -> {count}")
