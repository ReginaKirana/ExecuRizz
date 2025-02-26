# Difficulty level : Easy
# Number           : 4
# Title            : Belanjaan Budi
# ---------------------------------------------------------------------------------

# Seorang pedagang memiliki **N** kotak telur, masing-masing berisi sejumlah telur tertentu, 
# dan ia ingin menemukan dua kotak berbeda yang jumlah total telurnya tepat **X** butir. 
# Diberikan daftar berisi **N** bilangan bulat yang mewakili jumlah telur di setiap kotak, 
# temukan dan cetak indeks dua kotak tersebut dalam urutan menaik (indeks berbasis 0). 
# Dijamin selalu ada tepat satu pasangan yang memenuhi kondisi ini.

# ---------------------------------------------------------------------------------
def find_egg_cartons(X, N, A):
    index_map = {}
    
    for i, eggs in enumerate(A):
        complement = X - eggs
        if complement in index_map:
            return sorted([index_map[complement], i])
        index_map[eggs] = i

# Membaca input
X = int(input().strip())
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Menjalankan fungsi dan mencetak hasil
result = find_egg_cartons(X, N, A)
print(result[0], result[1])