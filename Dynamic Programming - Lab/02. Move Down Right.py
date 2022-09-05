from collections import deque

rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1
result = deque()
while True:
    result.appendleft([row, col])
    if row == 0 and col == 0:
        break
    if dp[row][col - 1] > dp[row - 1][col]:
        col -= 1
    else:
        row -= 1


print(deque)