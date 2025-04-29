import heapq

def a_star(start, goal):
    open_set = [(0, start)]  # Priority queue (f-score, node)
    g = {start: 0}  # Cost from start
    parents = {start: None}  

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]  # Return reversed path

        for neighbor, weight in Graph_nodes.get(current, []):
            new_cost = g[current] + weight
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                heapq.heappush(open_set, (new_cost + heuristic(neighbor), neighbor))
                parents[neighbor] = current

    return None  # No path found

def heuristic(node):
    H_dist = {'A': 13, 'B': 12, 'C': 4, 'D': 7, 'E': 3, 'F': 8, 'G': 2, 'H': 0}
    return H_dist.get(node, float('inf'))

Graph_nodes = {
    'A': [('B', 2), ('C', 2),('H',7)],
    'B': [('D', 4), ('E', 6)],
    'C': [('F', 3), ('G', 2)],
    'D': [],
    'E': [],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

print(a_star('A', 'H'))