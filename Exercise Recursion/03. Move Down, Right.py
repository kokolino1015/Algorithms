def find_all_ways(row, col, max_row, max_col):
    if row == max_row - 1 and col == max_col - 1:
        return 1
    if row == max_row or col == max_col:
        return 0

    result = 0
    result += find_all_ways(row + 1, col, max_row, max_col)
    result += find_all_ways(row, col + 1, max_row, max_col)
    return result


rows = int(input())
cols = int(input())
print(find_all_ways(0, 0, rows, cols))
