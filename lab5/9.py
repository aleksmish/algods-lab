arr = list(map(float, input("Введите элементы массива через пробел: ").split()))
n = len(arr)
last_max_pos = 0

for i in range(n):
    left_ok = (i == 0) or (arr[i] > arr[i - 1])
    right_ok = (i == n - 1) or (arr[i] > arr[i + 1])
    if left_ok and right_ok:
        last_max_pos = i + 1  # Порядковый номер с 1

print("Номер последнего локального максимума:", last_max_pos)
