def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def jump_search(arr: list[int], tagert: int) -> int:
    n = len(arr)
    step = int(n**0.5)
    prev = 0
    while arr[min(step, n) - 1] < tagert:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while arr[prev] < tagert:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == tagert:
        return prev
    return -1
