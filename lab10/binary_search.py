def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid

        elif mid_val > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    sorted_array = input("Введите сортированные числа через пробел: ")
    numbers = [int(x) for x in sorted_array.split()]
    target = int(input("Введите искомое число: "))
    result_found = binary_search(numbers, target)
    print(f"Результат: {result_found}")