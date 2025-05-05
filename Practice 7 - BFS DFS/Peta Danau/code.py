def count_danau(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*m for _ in range(n)]
    # Directions for flood fill
    orth = [(-1,0),(1,0),(0,-1),(0,1)]
    diag = [(-1,-1),(-1,1),(1,-1),(1,1)]
    all_dir = orth + diag

    # 1. Remove rivers: flood fill all water cells reachable from borders using 4-connectivity
    from collections import deque
    q = deque()
    # enqueue border water cells
    for i in range(n):
        for j in [0, m-1]:
            if grid[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))
    for j in range(m):
        for i in [0, n-1]:
            if grid[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))
    # BFS for rivers
    while q:
        x,y = q.popleft()
        for dx,dy in orth:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

    # 2. Count lakes using 8-directional connectivity on remaining water cells
    def dfs_mark(i,j):
        stack = [(i,j)]
        visited[i][j] = True
        while stack:
            x,y = stack.pop()
            for dx,dy in all_dir:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx,ny))

    lake_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and not visited[i][j]:
                # found a lake
                lake_count += 1
                dfs_mark(i,j)
    return lake_count


import sys
data = sys.stdin.read().strip().split()
x, y = map(int, data[:2])
vals = list(map(int, data[2:]))
grid = [vals[i*y:(i+1)*y] for i in range(x)]
print(count_danau(grid))