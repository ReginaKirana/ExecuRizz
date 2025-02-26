# Difficulty level : Medium
# Number           : 2
# Title            : Height Difference
# ---------------------------------------------------------------------------------

# Diberikan sebuah deret berisi nn bilangan bulat yang merepresentasikan ketinggian suatu jalur perjalanan, 
# di mana setiap nilai menunjukkan ketinggian pada titik tertentu. 
# Tentukan perbedaan ketinggian maksimum antara dua titik berurutan yang merupakan 
# puncak (bukit) atau lembah dalam jalur tersebut. 
# Sebuah titik dianggap sebagai puncak jika ketinggiannya lebih besar atau 
# sama dengan titik setelahnya dan lebih besar dari titik sebelumnya. 
# Sebuah titik dianggap sebagai lembah jika ketinggiannya lebih kecil atau 
# sama dengan titik setelahnya dan lebih kecil dari titik sebelumnya. 
# Pastikan titik pertama dan terakhir selalu dimasukkan dalam perhitungan sebagai bagian dari bukit atau lembah. 
# Cetak nilai perbedaan ketinggian maksimum antara dua titik bukit atau lembah yang berurutan.

# ---------------------------------------------------------------------------------
def max_height_difference():
    n = int(input().strip())  # Membaca jumlah data ketinggian
    heights = list(map(int, input().strip().split()))  # Membaca daftar ketinggian

    peaks_and_valleys = [heights[0]]  # Menyimpan bukit dan lembah
    for i in range(1, n - 1):
        if (heights[i] > heights[i - 1] and heights[i] >= heights[i + 1]) or (heights[i] < heights[i - 1] and heights[i] <= heights[i + 1]):
            peaks_and_valleys.append(heights[i])
    peaks_and_valleys.append(heights[-1])  # Tambahkan titik terakhir

    # Cari beda ketinggian maksimum antara bukit dan lembah berikutnya
    max_difference = 0
    for i in range(len(peaks_and_valleys) - 1):
        max_difference = max(max_difference, abs(peaks_and_valleys[i] - peaks_and_valleys[i + 1]))

    print(max_difference)

# Contoh penggunaan
max_height_difference()