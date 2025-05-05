from collections import deque

def pathBFS(n, edges, start, target):
    # build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        if node == target:
            return True
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)

    return False

# read input
n = int(input().strip())
e = int(input().strip())
edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))
start, target = map(int, input().split())

# result
result = pathBFS(n, edges, start, target)
print(result)