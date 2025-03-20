## Spy x Family Code: Blue
Loid Forger tengah menangani sebuah kasus misterius yang membutuhkan sejumlah petunjuk untuk dipecahkan. Ia memiliki tim agen rahasia, di mana setiap agen memiliki peringkat yang menggambarkan kecepatan mereka dalam mengumpulkan petunjuk. Diberikan sebuah array integer ranks di mana ranks[i] mewakili peringkat agen ke-i. Seorang agen dengan peringkat r dapat mengumpulkan n petunjuk dalam waktu r * n² menit.

Selain itu, diberikan sebuah integer clue yang mewakili total jumlah petunjuk yang harus dikumpulkan untuk menyelesaikan kasus tersebut.

Semua agen bekerja secara bersamaan dan Loid ingin meminimalkan waktu berpikir serta waktu eksekusi untuk mengumpulkan seluruh petunjuk. Tugas Anda adalah menentukan waktu minimum yang diperlukan agar seluruh petunjuk dapat dikumpulkan.

### Contoh: input:
4 2 3 1
10

### output:
16

### Explanation:
Agen dengan peringkat 4 mengumpulkan 2 petunjuk, waktu yang diperlukan adalah 4 * 2² = 16 menit.
Agen dengan peringkat 2 mengumpulkan 2 petunjuk, waktu yang diperlukan adalah 2 * 2² = 8 menit.
Agen dengan peringkat 3 mengumpulkan 2 petunjuk, waktu yang diperlukan adalah 3 * 2² = 12 menit.
Agen dengan peringkat 1 mengumpulkan 4 petunjuk, waktu yang diperlukan adalah 1 * 4² = 16 menit.

### Contoh 2: input:
5 1 8
6

### output:
16

### Explanation:
Agen dengan peringkat 5 mengumpulkan 1 petunjuk, waktu yang diperlukan adalah 5 * 1² = 5 menit.
Agen dengan peringkat 1 mengumpulkan 4 petunjuk, waktu yang diperlukan adalah 1 * 4² = 16 menit.
Agen dengan peringkat 8 mengumpulkan 1 petunjuk, waktu yang diperlukan adalah 8 * 1² = 8 menit.

### Input Format
Array of Integer
an Integer

### Constraints
1 ≤ jumlah agen (ranks.length) ≤ 10⁵
0 ≤ ranks[i] ≤ 100
1 ≤ jumlah petunjuk (clue) ≤ 10⁶

### Output Format
Integer

### Sample Input 0
4 2 3 1
10

### Sample Output 0
16

### Sample Input 1
5 1 8
6

### Sample Output 1
16