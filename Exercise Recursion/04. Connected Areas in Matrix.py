def find_areas(row, col, board, rows, cols):
    if row == rows or col == cols or row < 0 or col < 0:
        return 0
    if board[row][col] != '-':
        return 0
    board[row][col] = 'v'
    result = 1
    result += find_areas(row - 1, col, board, rows, cols)
    result += find_areas(row, col - 1, board, rows, cols)
    result += find_areas(row, col + 1, board, rows, cols)
    result += find_areas(row + 1, col, board, rows, cols)
    return result


rows = int(input())
cols = int(input())

board = []
[[board.append(' '.join(i).split()) for i in input().split()] for _ in range(rows)]
str_result = []
areas = 0
for j in range(rows):
    for i in range(cols):
        if board[j][i] == '-':
            areas += 1
            str_result.append((j, i, find_areas(j, i, board, rows, cols)))
str_result.insert(0, f'Total areas found: {areas}')
print(str_result[0])
str_result.pop(0)
index = 1
while True:
    if not len(str_result):
        break
    row_max, col_max, size_max = -9999999, -9999999, -9999999
    str_result_index = 0
    for i in range(0, len(str_result)):
        row, col, size = str_result[i]
        if size > size_max:
            row_max = row
            col_max = col
            size_max = size
            str_result_index = i
    print(f'Area #{index} at ({row_max}, {col_max}), size: {size_max}')
    str_result.pop(str_result_index)
    index += 1
