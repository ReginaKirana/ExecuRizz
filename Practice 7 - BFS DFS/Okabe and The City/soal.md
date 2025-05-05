## Okabe and City
Okabe suka bisa berjalan melalui kotanya di jalan setapak yang diterangi oleh lampu jalan. Dengan begitu, dia tidak dipukuli oleh anak-anak sekolah.

Kota Okabe diwakili oleh kisi-kisi sel 2D. Baris diberi nomor dari 1 hingga n dari atas ke bawah, dan kolom diberi nomor 1 hingga m dari kiri ke kanan. Tepat k sel di kota diterangi oleh lampu jalan. Dijamin bahwa sel kiri atas menyala.

Okabe memulai perjalanannya dari sel kiri atas, dan ingin mencapai sel kanan bawah. Tentu saja, Okabe hanya akan berjalan di atas sel yang menyala, dan dia hanya bisa bergerak ke sel yang berdekatan ke arah atas, bawah, kiri, dan kanan. Namun, Okabe juga dapat menyalakan sementara semua sel dalam satu baris atau kolom pada satu waktu jika dia membayar 1 koin, memungkinkannya untuk berjalan melalui beberapa sel yang tidak menyala pada awalnya.

Perhatikan bahwa Okabe hanya dapat menyalakan satu baris atau kolom pada satu waktu, dan harus membayar koin setiap kali dia menyalakan baris atau kolom baru. Untuk mengubah baris atau kolom yang menyala sementara, ia harus berdiri di sel yang menyala pada awalnya. Selain itu, setelah dia menghapus cahaya sementaranya dari baris atau kolom, semua sel dalam baris/kolom yang awalnya tidak menyala sekarang tidak menyala.

Bantu Okabe menemukan jumlah minimum koin yang harus dia bayar untuk menyelesaikan perjalanannya!

## format input :
Baris pertama input berisi tiga bilangan bulat yang dipisahkan spasi n, m, dan k (2 ≤ n, m, k ≤ 10000).

Masing-masing baris k berikutnya berisi dua bilangan bulat yang dipisahkan ruang ri dan ci (1 ≤ ri ≤ n, 1 ≤ ci ≤ m). baris dan kolom sel menyala ke-i.

Dijamin bahwa semua sel k berbeda. Dijamin bahwa sel kiri atas menyala.

### Input Format
Baris pertama input berisi tiga bilangan bulat yang dipisahkan spasi n, m, dan k (2 ≤ n, m, k ≤ 10000).

### Constraints
-

### Output Format
Cetak jumlah minimum koin yang harus dibayar Okabe untuk menyelesaikan perjalanannya, atau -1 jika tidak memungkinkan.

### Sample Input 0
4 4 5
1 1
2 1
2 3
3 3
4 3

### Sample Output 0
2