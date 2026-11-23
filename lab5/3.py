n = int(input("Введите N (> 2): "))
a = int(input("Введите A: "))
b = int(input("Введите B: "))

arr = [a, b]
current_sum = a + b
for i in range(2, n):
    arr.append(current_sum)
    current_sum += arr[-1]

print("Массив:", arr)
