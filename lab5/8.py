arr = list(map(float, input("Введите элементы массива через пробел: ").split()))
even_pos_elements = arr[1::2]
print("Минимум на четных номерах:", min(even_pos_elements))
