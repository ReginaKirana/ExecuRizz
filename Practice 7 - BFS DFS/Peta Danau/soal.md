## Peta Danau
Pada suatu hari ada seorang ilmuwan yang sedang menjelajahi sebuah wilayah, dalam perjalanannya ilmuwan tersebut menggunakan peta 2 dimensi yang di dalamnya disusun dengan angka 0 (wilayah air) dan 1 (wilayah daratan). Dari peta tersebut ilmuwan ingin mencari jumlah danau dan sungai dalam peta tersebut.

### Catatan:
- Danau adalah sebuah wilayah air yang dikelilingi oleh daratan sepenuhnya, jika ada bagian air yang menyentuh tepi peta tidak dianggap sebagai danau.
- Gunakan Algoritma Depth-First Search (DFS)

### Input Format
Baris pertama berisi dua bilangan bulat x dan y, masing-masing menunjukkan jumlah baris dan kolom peta.
Sebuah peta berbentuk matriks dengan x baris dan y kolom, dengan elemen matriks berupa digit 0 atau 1

### Constraints
1 ≤ m, n ≤ 10

### Output Format
Keluarkan satu baris yang menyatakan jumlah danau

### Sample Input 0
3 3
1 1 1
1 0 1
1 1 1

### Sample Output 0
1

### Sample Input 1
3 3
1 1 1
1 1 1
1 1 1

### Sample Output 1
0

### Sample Input 2
6 6
1 1 1 1 1 1
1 0 0 1 0 1
1 0 1 1 0 1
1 0 0 0 1 1
0 1 1 1 1 0
0 0 0 1 1 1

### Sample Output 2
1