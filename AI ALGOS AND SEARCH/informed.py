#path that looks closer we move towards it
#MAP DISTANCE GUESS = heuristic

#greedy best first search - it chooses the node that looks closest to the goal
#it does not care about how far we already traveled!!!

import heapq

def gbf(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[start], start)]

    while priority_queue:
        h , node = heapq.heappop(priority_queue)

        if node == goal:
            print('Reached goal', node)
            return
        if node not in visited:
            print('Visiting node', node)
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbour], neighbour))

#problem - sometimes it chooses bad paths, because actual cose traveled is ignored
#h(n) = estimated cost from node n to goal

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
heuristic = {
    'A': 5,
    'B': 3,
    'C': 0,
    'D': 6,
    'E': 4,
    'F': 9
}

gbf(graph, 'A', 'C',heuristic)

#A* python code

