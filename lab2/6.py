n = int(input("Введите число (1-999): "))

parity = "четное" if n % 2 == 0 else "нечетное"

if n < 10:
    digits = "однозначное"
elif n < 100:
    digits = "двузначное"
else:
    digits = "трехзначное"

print(f"{parity} {digits} число")
