arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
n = len(arr)

left, right = 0, n - 1
result = []
while left <= right:
    result.append(arr[left])
    if left != right:
        result.append(arr[right])
    left += 1
    right -= 1

print("Результат:", *result)
