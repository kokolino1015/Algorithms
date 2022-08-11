def dfs(marker, row, col, matrix, visited):
    if col < 0 or row < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] != marker:
        return
    if visited[row][col]:
        return
    visited[row][col] = True
    dfs(marker, row - 1, col, matrix, visited)
    dfs(marker, row + 1, col, matrix, visited)
    dfs(marker, row, col - 1, matrix, visited)
    dfs(marker, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = [[x for x in input()] for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
areas = 0
areas_letter = {}

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        areas += 1
        if key not in areas_letter:
            areas_letter[key] = 0
        areas_letter[key] += 1
areas_letter = sorted(areas_letter.items(), key=lambda x: x[0])
print(f'Areas: {areas}')
for key, value in areas_letter:
    print(f"Letter '{key}' -> {value}")