from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(' ')]
    graph[source].append(Edge(source, destination, weight))
    graph[destination].append(Edge(source, destination, weight))

start_node = int(input())
destination_node = int(input())

pq = PriorityQueue()
pq.put((-100, start_node))

distance = [float('-inf')] * nodes
distance[start_node] = 100

parent = [None] * nodes

while not pq.empty():
    max_distance, node = pq.get()
    if node == destination_node:
        break
    for edge in graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_distance = -max_distance * edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))
print(f'Most reliable path reliability: {distance[destination_node]:.2f}%')
path = deque()
node = destination_node
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep=' -> ')