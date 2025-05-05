from collections import deque

def min_ops(N):
    if N == 0:
        return 0

    # upper bound on states to explore
    MAX_STATE = 2 * N + 10

    # precompute powers of 3 up to MAX_STATE
    powers_of_3 = []
    p = 3
    while p <= MAX_STATE:
        powers_of_3.append(p)
        p *= 3

    visited = [False] * (MAX_STATE + 1)
    dist = [-1] * (MAX_STATE + 1)

    q = deque([N])
    visited[N] = True
    dist[N] = 0

    while q:
        x = q.popleft()
        d = dist[x]

        # if we reached 0, this is the minimum number of operations
        if x == 0:
            return d

        # 1) x -> x-1
        if x > 0 and not visited[x-1]:
            visited[x-1] = True
            dist[x-1] = d + 1
            q.append(x-1)

        # 2) x -> x+1
        if x + 1 <= MAX_STATE and not visited[x+1]:
            visited[x+1] = True
            dist[x+1] = d + 1
            q.append(x+1)

        # 3) x -> 2*x
        if 2 * x <= MAX_STATE and not visited[2*x]:
            visited[2*x] = True
            dist[2*x] = d + 1
            q.append(2*x)

        # 4) x -> x // (3^n) for any 3^n dividing x
        for p3 in powers_of_3:
            if p3 > x:
                break
            if x % p3 == 0:
                y = x // p3
                if not visited[y]:
                    visited[y] = True
                    dist[y] = d + 1
                    q.append(y)

    # should never get here since 0 is always reachable
    return -1

N = int(input().strip())
print(min_ops(N))