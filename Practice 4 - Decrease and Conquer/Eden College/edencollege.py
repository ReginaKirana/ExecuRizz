def mergeCount(arr, temp_arr, left, mid, right):
    i = left    # Indeks awal bagian kiri
    j = mid + 1  # Indeks awal bagian kanan
    k = left    # Indeks untuk temp_arr
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Hitung inversi
            j += 1
        k += 1
    
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def mergeSort_Count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += mergeSort_Count(arr, temp_arr, left, mid)
        inv_count += mergeSort_Count(arr, temp_arr, mid + 1, right)
        inv_count += mergeCount(arr, temp_arr, left, mid, right)
    return inv_count

def count_inversions(arr, N):
    temp_arr = [0] * N
    return mergeSort_Count(arr, temp_arr, 0, N - 1)

N = int(input())
arr = list(map(int, input().split()))
print(count_inversions(arr, N))