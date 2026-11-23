arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
seen = {}

for i, val in enumerate(arr):
    if val in seen:
        print("Номера одинаковых элементов:", seen[val] + 1, i + 1)
        break
    seen[val] = i
