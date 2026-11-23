def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

n = int(input("Введите число N "))
print(factorial(n))
