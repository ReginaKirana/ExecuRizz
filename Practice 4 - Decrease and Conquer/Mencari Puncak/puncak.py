def findPeak(arr, left, right):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:  # Bagian menurun, puncak ada di kiri
            right = mid
        else:  # Bagian menaik, puncak ada di kanan
            left = mid + 1
    return left + 1  # Mengembalikan index sesuai format (dimulai dari 1)
n = int(input())
arr = list(map(int, input().split()))
print(findPeak(arr, 0, n - 1))