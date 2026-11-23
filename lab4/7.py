def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_partitions(n: int, max_prime: int = None) -> list:
    if max_prime is None:
        max_prime = n
    if n == 0:
        return [[]]
    if n < 2:
        return []

    partitions = []
    for p in range(min(n, max_prime), 1, -1):
        if is_prime(p):
            for sub_partition in prime_partitions(n - p, p):
                partitions.append([p] + sub_partition)

    return partitions

n = int(input("Введите число N "))
print(prime_partitions(n))
