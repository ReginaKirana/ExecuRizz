# Difficulty level : Easy
# Number           : 3
# Title            : Koin Asing
# ---------------------------------------------------------------------------------

# Diberikan sebuah string sepanjang 8 karakter yang terdiri dari angka 1 hingga 9, 
# di mana setiap angka mewakili jenis koin yang muncul dalam sebuah set berisi 8 koin. 
# Di antara koin-koin tersebut, terdapat satu koin yang unik, 
# yaitu koin yang jumlah kemunculannya lebih sedikit dibandingkan koin lainnya. 
# Tentukan posisi (indeks berbasis 1) dari koin unik tersebut dalam urutan yang diberikan.

# Format Input: Sebuah string sepanjang 8 karakter yang hanya berisi angka 1 hingga 9, mewakili jenis koin.
# Format Output: Sebuah bilangan bulat yang menunjukkan posisi (indeks 1-based) dari koin yang berbeda tersebut.

# Contoh Input 1: 22332221
# Contoh Output 1:7
# (Pada input ini, koin dengan jenis 1 hanya muncul satu kali, yaitu di indeks ke-7 dalam indeks 1-based.)

# Contoh Input 2: 55556656
# Contoh Output 2:6
# (Koin dengan jenis 6 muncul hanya satu kali, yaitu di indeks ke-6 dalam indeks 1-based.)

# ---------------------------------------------------------------------------------
def find_unique_coin(coins):
    coin_count = {}
    
    # Hitung frekuensi setiap jenis koin
    for coin in coins:
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
    
    # Temukan jenis koin yang berbeda
    unique_coin = min(coin_count, key=coin_count.get)
    
    # Temukan indeks koin yang berbeda
    for i in range(8):
        if coins[i] == unique_coin:
            return i + 1  # Indeks dimulai dari 1
    
# Membaca input
coins = input().strip()
print(find_unique_coin(coins))