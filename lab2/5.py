n = int(input("Введите целое число: "))

if n == 0:
    print("нулевое число")
else:
    sign = "положительное" if n > 0 else "отрицательное"
    parity = "четное" if n % 2 == 0 else "нечетное"
    print(f"{sign} {parity} число")
