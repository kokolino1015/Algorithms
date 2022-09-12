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
    node, children_str = [x.strip() for x in command.split('->')]
    children = children_str.split()
    graph[node] = children
    command = input()
visited = set()
result = deque()
for node in graph:
    dfs(node, graph, visited, result)
print(*result, sep=' ')