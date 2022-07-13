def drawing_shapes(num):
    if num == 0:
        return
    print('*' * num)
    drawing_shapes(num - 1)
    print('#' * num)


number = int(input())


drawing_shapes(number)
