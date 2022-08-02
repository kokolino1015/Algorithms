numbers = [int(x) for x in input().split()]
numbers.sort()
print(' '.join([str(x) for x in numbers]))