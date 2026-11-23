M = int(input("Введите нечетное число M: "))
print(f"Введите квадратную матрицу порядка {M}: ")
A = [list(map(int, input().split())) for _ in range(M)]

result = []

for layer in range(M // 2):
    first = layer
    last = M - 1 - layer

    # Левый столбец (сверху вниз)
    for i in range(first, last):
        result.append(A[i][first])

    # Нижняя строка (слева направо)
    for j in range(first, last):
        result.append(A[last][j])

    # Правый столбец (снизу вверх)
    for i in range(last, first, -1):
        result.append(A[i][last])

    # Верхняя строка (справа налево)
    for j in range(last, first, -1):
        result.append(A[first][j])

# Последним добавляем центральный элемент матрицы
center = M // 2
result.append(A[center][center])

print("Вывод по спирали:")
print(*result)
