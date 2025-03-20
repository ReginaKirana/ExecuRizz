def compute_unhappiness(arr):
    n = len(arr)
    cost = [[0] * n for _ in range(n)]
    
    for i in range(n):
        black = white = 0
        for j in range(i, n):
            if arr[j] == 1:
                black += 1
            else:
                white += 1
            cost[i][j] = black * white
    
    return cost

def decrease_and_conquer(n, k, horses, cost, memo):
    if k == 1:
        return cost[0][n-1]  # Jika hanya ada satu kandang, seluruh kuda masuk ke sana
    if (n, k) in memo:
        return memo[(n, k)]
    
    min_unhappiness = float('inf')
    for i in range(1, n):  # Coba bagi di setiap titik
        left = decrease_and_conquer(i, k-1, horses, cost, memo)
        right = cost[i][n-1]  # Hitung ketidakbahagiaan untuk bagian kanan
        min_unhappiness = min(min_unhappiness, left + right)
    
    memo[(n, k)] = min_unhappiness
    return min_unhappiness

def solve(n, k, horses):
    cost = compute_unhappiness(horses)
    memo = {}
    return decrease_and_conquer(n, k, horses, cost, memo)

n, k = map(int, input().split())
horses = [int(input()) for _ in range(n)]
print(solve(n, k, horses))