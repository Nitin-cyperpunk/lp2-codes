def dfs(g, s, vis):
    vis[s] = 1
    print(f"DFS visiting: {s}")
    for c in g.get(s, []):
        if not vis[c]:
            dfs(g, c, vis)

def bfs(g, start, size):
    visited = [0] * size  # Initialize visited array
    queue = [start]       # Start with the starting node
    visited[start] = 1    # Mark the start node as visited
    print("BFS Traversal:")
    while queue:
        current = queue.pop(0)
        print(f"BFS visiting: {current}")
        for neighbor in g.get(current, []):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = 1

# User input
g = {}
size = int(input("Enter number of vertices (size of graph): "))

print("Enter adjacency list (list of neighbors) for each vertex.")
print("Example input for key=0: [1,2]")

for i in range(size):
    key = int(input(f"Enter node {i}: "))
    value = eval(input(f"Enter neighbors of node {key} as a list (e.g., [1,2]): "))
    g[key] = value

print("Graph:", g)

# DFS Traversal
vis = [0] * size
print("\nDFS Traversal:")
dfs(g, 0, vis)

# BFS Traversal
print("\nBFS Traversal:")
bfs(g, 0, size)
