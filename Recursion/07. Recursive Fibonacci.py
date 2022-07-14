def fibonacci(index, sequence, searched_pos):
    if index == searched_pos:
        print(sequence[index])
        return
    sequence.append(sequence[index] + sequence[index-1])
    fibonacci(index+1, sequence, searched_pos)


searched_pos = int(input())
sequence = [1, 1]
fibonacci(1, sequence, searched_pos)
