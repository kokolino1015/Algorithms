numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
    min_idx = idx
    for current_idx in range(idx + 1, len(numbers)):
        if numbers[min_idx] > numbers[current_idx]:
            min_idx = current_idx
    numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(*numbers, sep=' ')

