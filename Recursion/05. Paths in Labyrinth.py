def find_all_paths(row, col, labyrinth, direction, path):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return
    if labyrinth[row][col] == '*':
        return
    if labyrinth[row][col] == 'v':
        return

    path.append(direction)
    if labyrinth[row][col] == 'e':
        print(''.join(path))
    else:
        labyrinth[row][col] = 'v'
        find_all_paths(row - 1, col, labyrinth, 'U', path)
        find_all_paths(row + 1, col, labyrinth, 'D', path)
        find_all_paths(row, col - 1, labyrinth, 'L', path)
        find_all_paths(row, col + 1, labyrinth, 'R', path)
        labyrinth[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())

lab = []
for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, '', [])
