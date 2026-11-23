a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a != b:
    max_val = max(a, b)
    a = b = max_val
else:
    a = b = 0

print(f"A = {a}, B = {b}")
