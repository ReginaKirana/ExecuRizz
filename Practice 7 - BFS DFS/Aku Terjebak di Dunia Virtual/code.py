import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def count_zonaAman(grid, n, m):
    visited = [[False]*m for _ in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                # Mulai DFS iteratif dari (i,j)
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and grid[nx][ny] == 1:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                count += 1
    return count

def duniaVirtual():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(count_zonaAman(grid, n, m))

duniaVirtual();