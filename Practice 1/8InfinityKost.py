# Difficulty level : Medium
# Number           : 8
# Title            : Infinity Kost
# ---------------------------------------------------------------------------------

# Diberikan sebuah bilangan bulat n, buat urutan token yang terdiri dari bilangan Fibonacci 
# dan huruf alfabet dengan pola tertentu. Urutan dimulai dengan kelompok pertama-
# yang berisi 1 angka Fibonacci, diikuti oleh huruf A. 
# Kelompok kedua berisi 2 angka Fibonacci berikutnya, diikuti oleh huruf B, 
# kelompok ketiga berisi 3 angka Fibonacci, diikuti oleh huruf C, dan seterusnya. 
# Proses ini berlanjut hingga jumlah token yang dihasilkan mencapai n. 
# Jika dalam suatu kelompok jumlah token sudah mencapai n, 
# maka proses berhenti tanpa menambahkan token tambahan. 
# Cetak hasil urutan token tersebut dalam satu baris dengan setiap elemen dipisahkan oleh spasi.

# ---------------------------------------------------------------------------------
def main():
    import sys
    # Baca input, pastikan menghapus spasi dan newline
    n = int(sys.stdin.read().strip())
    
    result = []
    # Inisialisasi untuk deret Fibonacci
    a, b = 1, 1
    group = 1  # Kelompok ke-i
    
    # Selama jumlah token kurang dari n, lanjutkan membangun pola
    while len(result) < n:
        # Tambahkan i buah angka Fibonacci sesuai kelompok
        for _ in range(group):
            if len(result) < n:
                result.append(str(a))
                a, b = b, a + b
            else:
                break
        # Tambahkan huruf alfabet untuk kelompok tersebut jika masih memungkinkan
        if len(result) < n:
            # Huruf yang digunakan: A untuk kelompok 1, B untuk kelompok 2, dan seterusnya
            letter = chr(65 + group - 1)
            result.append(letter)
        group += 1

    # Output token yang telah dikumpulkan, pisahkan dengan spasi
    print(" ".join(result))

if __name__ == "__main__":
    main()