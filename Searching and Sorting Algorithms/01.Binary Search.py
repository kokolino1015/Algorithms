def find_number(numbers, index):
    middle = len(numbers) // 2
    if index > middle:
        pass
    else:
        pass


list_of_numbers = [int(x) for x in input().split(", ")]
list_of_numbers.sort()
print(find_number(list_of_numbers, 2))
