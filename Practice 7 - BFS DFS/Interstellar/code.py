import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def unite(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return
    if rank[u_root] < rank[v_root]:
        u_root, v_root = v_root, u_root
    parent[v_root] = u_root
    if rank[u_root] == rank[v_root]:
        rank[u_root] += 1
    # update the minimum warp cost for the new root
    if min_cost[v_root] < min_cost[u_root]:
        min_cost[u_root] = min_cost[v_root]

def interstellar():
    N, M, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    # initialize
    global parent, rank, min_cost
    parent = list(range(N+1))
    rank = [0] * (N+1)
    min_cost = [0] * (N+1)
    for i in range(1, N+1):
        min_cost[i] = A[i]

    # read the M connections
    for _ in range(M):
        u, v = map(int, input().split())
        unite(u, v)

    # read the journey of Q+1 planets
    journey = list(map(int, input().split()))

    total = 0
    for i in range(len(journey) - 1):
        u = journey[i]
        v = journey[i+1]
        ru = find(u)
        rv = find(v)
        if ru != rv:
            # not connected in the graph: pay warp_cost[ru] + warp_cost[rv]
            total += min_cost[ru] + min_cost[rv]

    print(total)

interstellar()