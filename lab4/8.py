def count_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

n = int(input("Введите число N "))
print(count_digits(n))
