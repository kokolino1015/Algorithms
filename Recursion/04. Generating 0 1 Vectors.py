def vector_creator(idx, vector):
    if len(vector) <= idx:
        print(*vector, sep="")
        return
    for num in range(2):
        vector[idx] = num
        vector_creator(idx + 1, vector)


n = int(input())

vector = [0] * n

vector_creator(0, vector)
