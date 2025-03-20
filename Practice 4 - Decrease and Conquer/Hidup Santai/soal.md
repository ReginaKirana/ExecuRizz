## Aku Ingin Hidup Santai
Setiap hari, Shiroe mengeluarkan semua kudanya, sehingga mereka dapat berlari dan bermain. Ketika mereka selesai, petani Ion harus membawa semua kuda kembali ke kandang. Untuk melakukan ini, ia menempatkan mereka dalam garis lurus dan mereka mengikutinya ke kandang. Karena mereka sangat lelah, ion petani memutuskan bahwa dia tidak ingin membuat kuda bergerak lebih dari yang seharusnya. Jadi ia mengembangkan algoritma ini: ia menempatkan kuda P1 ke -1 di kandang pertama, P2 berikutnya di kandang ke -2 dan sebagainya. Selain itu, dia tidak ingin kandang K yang dia miliki untuk kosong, dan tidak ada kuda yang harus ditinggalkan di luar. Sekarang Anda harus tahu bahwa ion petani hanya memiliki kuda hitam atau putih, yang tidak terlalu rukun. Jika ada saya kuda hitam dan kuda putih di satu kandang, maka koefisien ketidakbahagiaan kandang itu adalah i*j. Koefisien total ketidakbahagiaan adalah jumlah koefisien ketidakbahagiaan dari setiap kandang.

Tentukan cara untuk menempatkan kuda N ke kandang K, sehingga koefisien total ketidakbahagiaan diminimalkan.

format input : Pada baris pertama ada 2 angka: n (1 ≤ n ≤ 500) dan k (1 ≤ k ≤ n). Pada garis N berikutnya ada N angka. i-th dari garis-garis ini berisi warna kuda i-th dalam urutan: 1 berarti kuda itu hitam, 0 berarti kuda itu putih.

#### Contoh:
#### Input:
    6 3
    1
    1
    0
    1
    0
    1

#### Output:
    2

#### Input Format
    n (1 ≤ n ≤ 500) dan k (1 ≤ k ≤ n). 
Pada garis N berikutnya ada N angka. i-th dari garis-garis ini berisi warna kuda i-th dalam urutan: 1 berarti kuda itu hitam, 0 berarti kuda itu putih.

#### Constraints
    -

#### Output Format
    Integer

#### Sample Input 0
    6 3
    1
    1
    0
    1
    0
    1

#### Sample Output 0
    2