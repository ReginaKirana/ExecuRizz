## Island Counter
Diberikan sebuah grid 2D yang berisi 0 (lautan) dan 1 (daratan), hitunglah jumlah pulau yang ada. Sebuah pulau dibentuk oleh sel-sel daratan yang terhubung secara vertikal atau horizontal (tidak diagonal). Anda diminta menggunakan algoritma Depth-First Search (DFS) untuk menyelesaikan masalah ini.

## Input Format
Baris pertama berisi dua bilangan bulat m dan n, masing-masing menunjukkan jumlah baris dan kolom grid.
Diikuti oleh m baris, masing-masing berisi n digit (0 atau 1) yang dipisahkan oleh spasi.

## Constraints
1 ≤ m, n ≤ 100
Setiap elemen grid adalah 0 atau 1

## Output Format
Satu baris berisi jumlah pulau yang terdeteksi dalam grid.

## Sample Input 0
3 3
1 1 0
0 1 0
1 0 1

## Sample Output 0
3

## Sample Input 1
3 3
1 0 1
0 1 0
1 0 1

## Sample Output 1
5