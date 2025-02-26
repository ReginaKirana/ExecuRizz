# Difficulty level : Easy
# Number           : 7
# Title            : Per-Selisih-An
# ---------------------------------------------------------------------------------

# Diberikan sebuah array arr yang terdiri dari bilangan bulat, 
# temukan dan cetak selisih minimum antara dua elemen yang berdekatan setelah-
# array diurutkan dalam urutan naik. 
# Selisih minimum dihitung sebagai perbedaan terkecil antara dua elemen yang berurutan dalam 
# array yang telah diurutkan.

# ---------------------------------------------------------------------------------
def min_difference(arr):
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i + 1] - arr[i])
    
    return min_diff

# Membaca input
arr = list(map(int, input().strip().split()))
print(min_difference(arr))