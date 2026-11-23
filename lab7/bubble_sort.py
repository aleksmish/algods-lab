def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    raw_input = input("Введите массив чисел: ")
    numbers = [int(x) for x in raw_input.split()]

    sorted_numbers = bubble_sort(numbers)
    print("Сортированный массив:", *sorted_numbers)
