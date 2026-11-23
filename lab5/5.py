arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
n = len(arr)

# Нечетные порядковые номера (1, 3, 5...) соответствуют четным индексам (0, 2, 4...)
odd_positions = [arr[i] for i in range(0, n, 2)]

# Четные порядковые номера (2, 4, 6...) соответствуют нечетным индексам (1, 3, 5...)
even_positions = [arr[i] for i in range(1, n, 2)][::-1]

print("Результат:", *(odd_positions + even_positions))
