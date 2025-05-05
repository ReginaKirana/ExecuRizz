import sys
sys.setrecursionlimit(1000000)

def islands(grid, m, n):
    visited = [[False]*n for _ in range(m)]
    islands = 0

    # empat arah gerakan: atas, bawah, kiri, kanan
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                # baru ketemu pulau, DFS untuk menandai seluruh selnya
                islands += 1
                stack = [(i, j)]
                visited[i][j] = True

                while stack:
                    x, y = stack.pop()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
    return islands

m, n = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
print(islands(grid, m, n))