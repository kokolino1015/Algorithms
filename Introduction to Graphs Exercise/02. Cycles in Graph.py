def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_note_without_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node
    return None


graph = {}

command = input()
while command != 'End':
    start, end = command.split('-')
    if start not in graph:
        graph[start] = []
    graph[start].append(end)
    command = input()

dependencies = find_dependencies(graph)
is_acyclic = True
while dependencies:
    node_to_remove = find_note_without_dependencies(dependencies)
    if not node_to_remove:
        is_acyclic = False
        break
    dependencies.pop(node_to_remove)
    if len(dependencies) < 1:
        break
    if node_to_remove in graph:
        for children in graph[node_to_remove]:
            dependencies[children] -= 1
if is_acyclic:
    print('Acyclic: Yes')
else:
    print('Acyclic: No')