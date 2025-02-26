# Fifficulty level : Medium
# Number           : 1
# Title            :Foto Festival Terbaik
# ---------------------------------------------------------------------------------

# Diberikan sebuah matriks berukuran N×MN×M yang berisi bilangan bulat, 
# carilah sub-matriks berbentuk persegi yang memiliki total kualitas terbesar, 
# di mana kualitas suatu sub-matriks didefinisikan sebagai jumlah semua elemen di dalamnya. 
# Jika terdapat beberapa sub-matriks dengan kualitas yang sama, pilih sub-matriks dengan ukuran terbesar. 
# Jika masih ada hasil yang sama, pilih yang posisinya lebih atas, dan jika masih sama, pilih yang lebih ke kiri. 
# Cetak total kualitas terbaik, ukuran sub-matriks, 
# serta koordinat baris dan kolom (1-based) dari sudut kiri atas sub-matriks tersebut.

# ---------------------------------------------------------------------------------
def find_best_photo(N, M, matrix):
    best_quality = float('-inf')
    best_size = 0
    best_x, best_y = 0, 0
    
    # Coba semua ukuran sub-matriks
    for size in range(1, min(N, M) + 1):
        for i in range(N - size + 1):
            for j in range(M - size + 1):
                # Hitung jumlah elemen dalam sub-matriks ukuran size x size
                total_quality = sum(matrix[x][y] for x in range(i, i + size) for y in range(j, j + size))
                
                # Perbarui jika menemukan kualitas lebih tinggi
                if (total_quality > best_quality or
                    (total_quality == best_quality and size > best_size) or
                    (total_quality == best_quality and size == best_size and i < best_x) or
                    (total_quality == best_quality and size == best_size and i == best_x and j < best_y)):
                    best_quality = total_quality
                    best_size = size
                    best_x, best_y = i, j
    
    print(best_quality, best_size, best_x + 1, best_y + 1)
    
# Contoh Input
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

find_best_photo(N, M, matrix)