#DEFINE - try everything and no smart guessing - THE BLIND EXPLORER
#BFS

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


bfs(graph, 'A')

print('\n')

# DFS - DIG A TUNNEL , if close return and start from another point

def dfs(graph, node , visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
           dfs(graph, neighbor, visited)

dfs(graph, 'A')


#UCS - Cheapest path always
import heapq
def ucs(graph, start):
    visited = set()
    priority_queue = [(0, start)]
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node not in visited:
            print(node, 'Cost', cost)
            visited.add(node)

            for neighbor,weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + weight, neighbor))

graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}

print('\n')
ucs(graph1, 'A')
