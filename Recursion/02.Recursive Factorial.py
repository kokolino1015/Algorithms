def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)


num = int(input())
print(factorial(num))