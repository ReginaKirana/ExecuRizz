## Anya dan Ujian di Eden College
Anya Forger sedang belajar di Eden College dan ingin menjadi murid terbaik untuk mendapatkan Stella ⭐!

Setiap minggu, Eden College mengumumkan daftar nilai ujian murid-muridnya. Namun, semakin tidak teratur daftar tersebut, semakin sulit bagi Damian Desmond untuk menerima hasilnya!

Anya ingin mengetahui seberapa tidak teratur daftar nilai ujian. Ia mendefinisikan ketidakteraturan sebagai jumlah inversi dalam daftar nilai.

Inversi terjadi jika ada dua nilai (i, j) dengan i < j, tetapi nilai[i] > nilai[j].

Bantu Anya menghitung jumlah inversi dalam daftar nilai ujian teman-temannya!

#### Input Format
Baris pertama berisi bilangan bulat N (1 ≤ N ≤ 100000), jumlah murid Eden College. Baris kedua berisi N bilangan bulat yang menunjukkan nilai ujian murid-murid dalam urutan yang diumumkan oleh sekolah. (1 ≤ nilai ≤ 100000)

#### Constraints
    (1 ≤ N ≤ 100000) (1 ≤ nilai ≤ 100000)

#### Output Format
Cetak satu bilangan bulat, yaitu jumlah inversi dalam daftar nilai.

#### Sample Input 0
    5   
    2 4 1 3 5

#### Sample Output 0
    3

#### Explanation 0
    Daftar nilai murid: [2, 4, 1, 3, 5]
    Terdapat 3 inversi:
    (4,1) → 4 lebih dulu tetapi lebih besar dari 1
    (2,1) → 2 lebih dulu tetapi lebih besar dari 1
    (4,3) → 4 lebih dulu tetapi lebih besar dari 3

#### Sample Input 1
    4
    10 20 30 40

#### Sample Output 1
    0