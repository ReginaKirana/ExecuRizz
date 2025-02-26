# Difficulty level : Medium
# Number           : 4
# Title            : Himmel Sang Looter
# ---------------------------------------------------------------------------------

# Diberikan sebuah array arr yang terdiri dari n bilangan bulat, 
# temukan dan cetak jumlah maksimum dari subarray contiguous (berurutan) dalam array tersebut. 
# Subarray adalah bagian dari array yang mempertahankan urutan elemen asli. 
# Jika semua elemen negatif, pilih elemen dengan nilai terbesar.

# ---------------------------------------------------------------------------------
def max_subarray_sum(n, arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Membaca input sesuai format HackerRank
n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(max_subarray_sum(n, arr))