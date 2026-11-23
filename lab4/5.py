def binary_search(arr: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

nums = list(map(int, input("Введите массив ").split()))
target = int(input("Введите искомое число "))
print(binary_search(nums, target, 0, len(nums) - 1))
