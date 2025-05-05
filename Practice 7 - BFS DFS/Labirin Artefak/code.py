import sys
sys.setrecursionlimit(1000000)

def count_artefak(grid, n, m, start_r, start_c):
    visited = [[False]*m for _ in range(n)]
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True
    count = 0

    # four directions: up, down, left, right
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        r, c = stack.pop()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    if grid[nr][nc] == 'A':
                        count += 1
                    stack.append((nr, nc))
    return count

def LabirinArtefak():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    grid = []
    start_r = start_c = None

    for i in range(n):
        row = input().split()
        for j, ch in enumerate(row):
            if ch == 'Y':
                start_r, start_c = i, j
        grid.append(row)

    result = count_artefak(grid, n, m, start_r, start_c)
    print(result)

LabirinArtefak()