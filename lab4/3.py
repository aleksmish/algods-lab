def power(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    return x * power(x, n - 1)

x = int(input("Введите число X "))
n = int(input("Введите число N "))
print(power(x, n))  
