## Level Graph
Diberikan sebuah graph tak berarah dan tak berbobot dengan 5 simpul, dinomori 1 sampai 5, dan beberapa sisi. Mulai dari simpul 1, cari level (jarak dalam jumlah sisi) ke setiap simpul lain menggunakan BFS. Tulis urutan kunjungan BFS dan tentukan jarak (level) dari simpul 1 ke setiap simpul.

### Input Format
5 [[1,2], [2,3], [1,4], [4,5]] 1

### Constraints
-

### Output Format
Urutan BFS: 1, 2, 4, 3, 5 Level: simpul 1: 0 simpul 2: 1 simpul 4: 1 simpul 3: 2 simpul 5: 2

### Sample Input 0
4
[[1,2], [1,3], [2,4]]  
1

### Sample Output 0
Urutan BFS: 1, 2, 3, 4
Level:
simpul 1: 0
simpul 2: 1
simpul 3: 1
simpul 4: 2

### Sample Input 1
6
[[1,2], [2,3], [2,4], [1,5], [5,6]]  
2

### Sample Output 1
Urutan BFS: 2, 1, 3, 4, 5, 6
Level:
simpul 2: 0
simpul 1: 1
simpul 3: 1
simpul 4: 1
simpul 5: 2
simpul 6: 3