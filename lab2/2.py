a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

result = (a + b + c) - min(a, b, c)
print("Сумма двух наибольших:", result)
