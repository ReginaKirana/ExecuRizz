def MissingNumber():
    # Input
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    # List untuk menandai kehadiran angka dari 0 sampai n
    present = [False] * (n + 1)
    for num in arr:
        if 0 <= num <= n:
            present[num] = True

    # Cari angka yang hilang dari rentang [0, n]
    for num in range(n, -1, -1):
        if not present[num]:
            print(num)
            break
            
MissingNumber()