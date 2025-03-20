def find_missingNumber(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] != mid:
            if mid == 0 or arr[mid - 1] == mid - 1:
                return mid
            right = mid - 1
        else:
            left = mid + 1
    
    return len(arr)  # Jika semua urutan benar, yang hilang adalah N

N = int(input().strip())
arr = list(map(int, input().strip().split()))
print(find_missingNumber(arr))