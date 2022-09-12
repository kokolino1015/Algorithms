from collections import deque


def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, result)
    result.appendleft(node)


graph = {}

command = input()
while command != 'End':
    args = [x.strip() for x in command.split('->')]
    if len(args) == 1:
        graph[args[0]] = []
    else:
        graph[args[0]] = args[1].split(' ')
    command = input()
visited = set()
result = deque()
for node in graph:
    dfs(node, graph, visited, result)
print(*result, sep=' ')