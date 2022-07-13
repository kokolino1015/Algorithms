def sum_elements(nums, param):
    if param == len(nums) - 1:
        return nums[param]
    return nums[param] + sum_elements(nums, param + 1)


nums = [int(x) for x in input().split()]
print(sum_elements(nums, 0))
