def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1
    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)
    salaries[node] = salary
    return salary


nodes = int(input())
graph = {}

for person in range(nodes):
    graph[person] = []
    for employ, value in enumerate(input()):
        if value == 'Y':
            graph[person].append(employ)

salaries = [None] * nodes
result = 0
for node in range(nodes):
    salary = dfs(node, graph, salaries)
    result += salary
print(result)
