def binary_search(left, right, numbers, target):
    if left > right:
        return -1
    else:
        mid_idx = (left + right) // 2
        if numbers[mid_idx] == target:
            return mid_idx
        elif target > numbers[mid_idx]:
            left = mid_idx + 1
            return binary_search(left, right, numbers, target)
        else:
            right = mid_idx - 1
            return binary_search(left, right, numbers, target)


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(0, len(numbers) - 1, numbers, target))
