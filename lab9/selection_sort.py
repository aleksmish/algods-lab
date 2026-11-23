def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    raw_input = input("Введите числа через пробел: ")
    numbers = [int(x) for x in raw_input.split()]

    sorted_numbers = selection_sort(numbers)
    print("Отсортированный массив:", *sorted_numbers)
