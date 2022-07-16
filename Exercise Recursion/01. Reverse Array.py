# Without recursion
# print(*list(reversed(input().split())), sep=' ')

# With recursion
# 1
def reverse_array(numbers, index, new_array):
    if index == -1:
        print(*new_array, sep=' ')
        return
    new_array.append(numbers.pop(index))
    reverse_array(numbers, index - 1, new_array)


list_of_numbers = input().split()
reverse_array(list_of_numbers, len(list_of_numbers) - 1, [])

# 2
# def rev(idx, elements):
#     if idx == len(elements) // 2:
#         return
#     swap_idx = len(elements) - 1 - idx
#     elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
#     rev(idx+1, elements)
#
#
# rev(0, list_of_numbers)
# print(*list_of_numbers,sep=" ")

