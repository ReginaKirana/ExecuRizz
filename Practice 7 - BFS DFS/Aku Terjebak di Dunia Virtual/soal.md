## Aku terjebak di dunia virtual
Di dunia virtual, seorang pemain video game sedang terjebak dalam labirin berisi monster. Labirin tersebut digambarkan dalam bentuk matriks, di mana 1 menunjukkan area yang dapat dilalui pemain dan 0 menunjukkan dinding. Pemain harus menemukan dan menghitung jumlah zona aman yang dapat dijelajahi tanpa bertemu monster.

Setiap zona aman (nilai 1) terhubung secara horizontal atau vertikal, namun tidak diagonal. Sementara zona berbahaya (nilai 0) tidak bisa dilewati.

### Catatan: 
- Gunakan Algoritma Depth-First Search (DFS)

### Input Format
Baris pertama: dua bilangan bulat n dan m, yang menunjukkan jumlah baris dan kolom pada matriks.
Diikuti n baris, masing-masing berisi m bilangan (0 atau 1) yang dipisahkan oleh spasi.

### Constraints
1 ≤ n, m ≤ 1000

### Output Format
Sebuah bilangan bulat yang menunjukkan jumlah zona aman yang dapat dijelajahi pemain.

### Sample Input 0
5 5
1 1 0 0 0
1 1 0 0 0
0 0 1 1 0
0 0 0 1 1
1 1 1 0 0

### Sample Output 0
3

### Sample Input 1
3 4
1 0 0 0
1 1 1 0
0 0 1 1

### Sample Output 1
1

### Sample Input 2
4 4
1 1 0 0
0 1 0 0
1 1 0 0
0 0 1 1

### Sample Output 2
2