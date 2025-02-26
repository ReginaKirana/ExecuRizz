# Difficulty level : Easy
# Number           : 4
# Title            : Operasi Daftar Bilangan
# ---------------------------------------------------------------------------------

# Diberikan sebuah daftar bilangan bulat numbers, 
# lakukan operasi khusus berdasarkan jumlah elemen dalam daftar. 
# Jika jumlah elemen genap, kembalikan hasil penjumlahan seluruh elemen. 
# Jika jumlah elemen ganjil, ambil nilai elemen tengah, 
# lalu jumlahkan semua elemen di sebelah kiri dan kanan elemen tengah, 
# kemudian kalikan hasilnya dengan nilai elemen tengah tersebut. 
# Cetak hasil akhir dari operasi ini.

# ---------------------------------------------------------------------------------
def special_operation(numbers):
    n = len(numbers)
    
    if n % 2 == 0:
        return sum(numbers)
    else:
        mid_index = n // 2
        middle_value = numbers[mid_index]
        left_sum = sum(numbers[:mid_index])
        right_sum = sum(numbers[mid_index + 1:])
        return (left_sum + right_sum) * middle_value

# Membaca input dan memprosesnya
numbers = list(map(int, input().split()))
result = special_operation(numbers)
print(result)