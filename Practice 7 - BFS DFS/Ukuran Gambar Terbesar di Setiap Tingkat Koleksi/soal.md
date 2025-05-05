## Ukuran Gambar Terbesar di Setiap Tingkat Koleksi
Dalam sebuah sistem galeri digital, gambar-gambar disusun dalam bentuk pohon biner. Setiap node dalam pohon mewakili sebuah gambar, dan nilai di node tersebut menunjukkan ukuran file gambar dalam megabyte (MB).

Sebagai kurator galeri, Anda diminta untuk menemukan ukuran gambar terbesar di setiap tingkat koleksi. Tingkat ke-0 adalah gambar root, tingkat ke-1 adalah anak-anak dari root, tingkat ke-2 adalah cucu-cucu, dan seterusnya.

Tugas kalian adalah menuliskan fungsi untuk mengembalikan sebuah list yang berisi ukuran gambar terbesar di setiap tingkat pohon, mulai dari tingkat 0.

### Input Format
Baris pertama: Jumlah node n Baris kedua: List node dalam bentuk level order, dengan null untuk node kosong

### Constraints
Jumlah node dalam pohon berada dalam rentang [0, 10^4]. -2^31 <= Node.value <= 2^31 - 1

### Output Format
Sebuah list integer, di mana setiap angka adalah ukuran gambar terbesar pada tingkat pohon yang bersangkutan, dipisahkan oleh spasi.

### Sample Input 0
1
5

### Sample Output 0
5

### Sample Input 1
7
1 3 2 5 3 null 9

### Sample Output 1
1 3 9