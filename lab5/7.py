arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
diff = arr[1] - arr[0]

is_progression = all(arr[i] - arr[i - 1] == diff for i in range(2, len(arr)))
print(diff if is_progression else 0)
