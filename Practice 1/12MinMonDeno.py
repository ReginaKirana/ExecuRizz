# Difficulty level : Easy
# Number           : 12
# Title            : Pecahan Uang Minimum
# ---------------------------------------------------------------------------------

# Diberikan sebuah jumlah uang X, tentukan jumlah minimum koin yang diperlukan-
# untuk mencapai nilai tersebut menggunakan denominasi koin yang tersedia: 50, 25, 10, 5, dan 1. 
# Setiap koin dapat digunakan sebanyak mungkin. 
# Cetak jumlah minimum koin yang dibutuhkan untuk membentuk X.

# ---------------------------------------------------------------------------------
def min_money(X, money=[50, 25, 10, 5, 1]):
    min_count = float('inf')
    
    def find_min(remaining, count):
        nonlocal min_count
        if remaining == 0:
            min_count = min(min_count, count)
            return
        if count >= min_count:
            return
        for m in money:
            if remaining >= m:
                find_min(remaining - m, count + 1)
    
    find_min(X, 0)
    return min_count

# Membaca input dari pengguna
X = int(input())
print(min_money(X))