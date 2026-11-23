n = int(input("Введите N: "))
a = float(input("Введите A: "))
d = float(input("Введите D: "))

arr = [a * (d ** i) for i in range(n)]
print(arr)
