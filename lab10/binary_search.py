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
    sorted_array = (2, 5, 8, 12, 16, 23, 38, 56, 72, 91)

    result_found = binary_search(sorted_array, 23)
    print(f"Результат: {result_found}")

    result_not_found = binary_search(sorted_array, 40)
    print(f"Результат: {result_not_found}")
