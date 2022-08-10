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


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

dependencies_by_node = find_dependencies(graph)
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_note_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        print("Invalid topological sorting")
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for children in graph[node_to_remove]:
        dependencies_by_node[children] -= 1
if not dependencies_by_node:
    print(f'Topological sorting: {", ".join(sorted_nodes)}')
