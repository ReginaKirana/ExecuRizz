## Temukan Novel
Soobin memiliki koleksi novel Omniscient Reader yang ditata urut berdasarkan edisi volumenya pada rak yang berupa sebuah array. Bantu Soobin untuk menemukan dimana letak index awal dan akhir dari volume novel yang dicari menggunakan algoritma BINARY SEARCH!

Jika edisi yang dicari tidak ditemukan akan mengeluarkan output berupa [-1, -1]

### Input Format
baris pertama merupakan array of integer yang pasti terurut. baris kedua merupakan target volume yang dicari berupa integer.

### Output Format
array yang berisi posisi awal dan akhir target. [awal, akhir]

### Sample Input 0
1 1 3 5 6 9 9
1

### Sample Output 0
[0, 1]

### Explanation 0
target = 1; dimana 1 paling awal ditemukan di index 0 dan 1 paling akhir ditemukan pada index 1

### Sample Input 1
1 2 3 4 5
8

### Sample Output 1
[-1, -1]

### Explanation 1
target = 8; tidak ditemukan pada array sehingga menggeluarkan [-1, -1]