a = int(input("Введите A: "))
b = int(input("Введите B (A < B): "))
for num in range(a, b + 1):
    for _ in range(num):
        print(num, end=" ")
