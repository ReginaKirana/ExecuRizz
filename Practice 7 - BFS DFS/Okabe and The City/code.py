import sys
from collections import deque

def Okabe():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    lamp = {}
    cells = []
    # read the k lit cells, index them 0..k-1
    for _ in range(k):
        r, c = map(int, input().split())
        if (r, c) not in lamp:
            lamp[(r, c)] = len(cells)
            cells.append((r, c))

    start = lamp[(1, 1)]
    base = len(cells)
    N = base + n + m + 1
    T = N - 1

    adj = [[] for _ in range(N)]

    # connect adjacent lit cells with cost 0
    for i, (r, c) in enumerate(cells):
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            j = lamp.get((r+dr, c+dc))
            if j is not None:
                adj[i].append((j, 0))

    # connect each lit cell to its row-node and column-node
    for i, (r, c) in enumerate(cells):
        row_node = base + (r-1)
        col_node = base + n + (c-1)
        # pay 1 coin to light row or column
        adj[i].append((row_node, 1))
        adj[i].append((col_node, 1))
        # once lit, you can move back to the cell for free
        adj[row_node].append((i, 0))
        adj[col_node].append((i, 0))

    # connect target cell into sink T
    if (n, m) in lamp:
        idx = lamp[(n, m)]
        adj[idx].append((T, 0))
    rown = base + (n-1)
    colm = base + n + (m-1)
    adj[rown].append((T, 0))
    adj[colm].append((T, 0))

    # 0-1 BFS from start to T
    INF = 10**9
    dist = [INF] * N
    dq = deque([start])
    dist[start] = 0

    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in adj[u]:
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    ans = dist[T]
    print(ans if ans < INF else -1)

Okabe()