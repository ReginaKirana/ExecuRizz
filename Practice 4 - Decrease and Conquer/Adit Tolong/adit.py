def min_balls(N, H, balls):
    balls.sort(reverse=True)
    count = 0 
    i = 0
    while H > 0 and i < N:
        if balls[i] <= H:
            count += H // balls[i]
            H %= balls[i]
        i += 1 
    return count if H == 0 else -1

data = input().split()
N, H = int(data[0]), int(data[1])
balls = list(map(int, input().split()))
print(min_balls(N, H, balls))