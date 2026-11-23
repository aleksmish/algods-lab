import math

M, N = map(int, input("Введите размеры M и N: ").split())
A = [list(map(int, input().split())) for _ in range(M)]
K = int(input(f"Введите номер строки K (от 1 до {M}): "))

target_row = A[K - 1]

row_sum = sum(target_row)
row_prod = math.prod(target_row)

print(f"Элементы {K}-й строки:", *target_row)
print("Сумма элементов:", row_sum)
print("Произведение элементов:", row_prod)
