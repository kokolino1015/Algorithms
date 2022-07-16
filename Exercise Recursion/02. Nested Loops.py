def nested_loops(index, list_of_nums):
    if index >= len(list_of_nums):
        print(*list_of_nums, sep=' ')
        return
    for number in range(1, len(list_of_nums) + 1):
        list_of_nums[index] = number
        nested_loops(index + 1, list_of_nums)


times = int(input())
list_of_numbers = [0] * times
nested_loops(0, list_of_numbers)
