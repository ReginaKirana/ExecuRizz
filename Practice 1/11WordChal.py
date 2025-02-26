# Difficulty level : Medium
# Number           : 11
# Title            : Tantangan Kata
# ---------------------------------------------------------------------------------

# Diberikan sebuah string yang berisi karakter yang tersedia dan-
# sebuah daftar angka yang merepresentasikan kode ASCII dari karakter yang ingin dibentuk, 
# tentukan apakah mungkin menyusun string target menggunakan karakter yang tersedia. 
# Setiap karakter dalam string hanya dapat digunakan sekali. Jika string target dapat dibentuk sepenuhnya, 
# cetak "Bisa"; jika tidak, cetak "Tidak". 
# Selain itu, cetak juga bagian dari string target yang berhasil disusun menggunakan karakter-
# yang tersedia sebelum kehabisan.

# ---------------------------------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    available = data[0].strip()
    # Baris kedua merupakan deretan angka yang merepresentasikan ASCII code.
    # Pisahkan dan ubah setiap angka menjadi karakter.
    numbers = data[1].split() if len(data) >= 2 else []
    target = ''.join(chr(int(num)) for num in numbers)
    
    # Buat frequency counter untuk karakter yang tersedia
    freq = Counter(available)
    constructed = []
    
    # Proses target karakter per karakter, membentuk prefix terpanjang yang mungkin.
    for ch in target:
        if freq[ch] > 0:
            freq[ch] -= 1
            constructed.append(ch)
        else:
            break
    
    # Jika seluruh target bisa disusun, maka hasilnya adalah "Bisa".
    if ''.join(constructed) == target:
        print("Bisa")
    else:
        print("Tidak")
    print(''.join(constructed))

if __name__ == '__main__':
    main()