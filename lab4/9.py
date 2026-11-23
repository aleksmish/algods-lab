def hanoi(n: int, source: str = "A", target: str = "C", auxiliary: str = "B") -> None:
    if n == 1:
        print(f"Переместить диск 1 со стержня {source} на стержень {target}")
        return

    # 1. Перемещаем n-1 дисков со стартового стержня на вспомогательный
    hanoi(n - 1, source, auxiliary, target)

    # 2. Перемещаем самый большой диск на целевой стержень
    print(f"Переместить диск {n} со стержня {source} на стержень {target}")

    # 3. Перемещаем n-1 дисков со вспомогательного на целевой
    hanoi(n - 1, auxiliary, target, source)

n = int(input("Введите число N "))
print(hanoi(n))
