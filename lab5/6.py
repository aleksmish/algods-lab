arr = list(map(float, input("Введите элементы массива через пробел: ").split()))
k = int(input("Введите K: "))
l = int(input("Введите L: "))

sub_arr = arr[k - 1 : l]
average = sum(sub_arr) / len(sub_arr)
print("Среднее арифметическое:", average)
