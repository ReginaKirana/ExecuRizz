def min_assignment_cost(N, C):
    min_cost = [float('inf')]
    assigned = [False] * N
    
    def backtrack(robot, current_cost):
        if robot == N:
            min_cost[0] = min(min_cost[0], current_cost)
            return
        
        if current_cost >= min_cost[0]:
            return
        
        for task in range(N):
            if not assigned[task]:
                assigned[task] = True
                backtrack(robot + 1, current_cost + C[robot][task])
                assigned[task] = False
    
    backtrack(0, 0)
    return min_cost[0]

# Input Langsung dari Soal
N = 4
C = [
    [15, 20, 35, 40],
    [25, 30, 10, 50],
    [30, 40, 20, 25],
    [20, 25, 15, 30]
]

# Output
print(min_assignment_cost(N, C))