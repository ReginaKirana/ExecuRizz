from collections import deque, defaultdict
import ast

def bfs_level(n, edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    level = [-1] * (n + 1)
    queue = deque()
    bfs_order = []

    queue.append(start)
    visited[start] = True
    level[start] = 0

    while queue:
        current = queue.popleft()
        bfs_order.append(current)
        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                level[neighbor] = level[current] + 1
                queue.append(neighbor)

    print("Urutan BFS:", ", ".join(map(str, bfs_order)))
    print("Level:")
    for node in bfs_order:
        print(f"simpul {node}: {level[node]}")

# ===== Input dari soal =====
n = int(input())  # jumlah simpul
edges = ast.literal_eval(input())  # list sisi
start = int(input())  # simpul awal
bfs_level(n, edges, start)