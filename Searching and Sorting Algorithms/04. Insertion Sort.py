numbers = [int(x) for x in input().split()]

for i in range(len(numbers)):
    j = i
    while j > 0 and numbers[j] < numbers[j - 1]:
        numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
        j -= 1

print(*numbers, sep=' ')
