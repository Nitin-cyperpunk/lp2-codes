import heapq
graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 4},
    'G': {}
}
heuristics = {'S': 5, 'A': 5, 'B': 4, 'C': 2, 'D': 6, 'G': 0}
def a_star(start, goal):
    pq = [(heuristics[start], 0, start, [])]  # (f = g + h, g, current_node, path_so_far)
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]  # Create a new list to avoid mutating shared path
        if node == goal:
            return path, g  # Found goal

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                total_cost = g + cost
                f_cost = total_cost + heuristics[neighbor]
                heapq.heappush(pq, (f_cost, total_cost, neighbor, path))

    return None, float('inf')  # No path found

# Run A* from 'S' to 'G'
path, cost = a_star('S', 'G')
print("Shortest Path:", path)
print("Total Cost:", cost)
