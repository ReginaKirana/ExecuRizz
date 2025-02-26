# Difficulty level : Easy
# Number           : 10
# Title            : Jangan coba-coba, nanti kecanduan
# ---------------------------------------------------------------------------------

# Diberikan sebuah daftar bilangan bulat coin_list yang merepresentasikan-
# jenis-jenis koin dan sebuah bilangan bulat target_coin yang menunjukkan jenis koin yang dicari, 
# tentukan indeks pertama dari target_coin dalam coin_list. Jika target_coin ditemukan dalam daftar, 
# kembalikan indeksnya (berbasis 0), tetapi jika tidak ditemukan, kembalikan string "Tidak ditemukan".

# ---------------------------------------------------------------------------------

def find_coin_index(coin_list, target_coin):
    try:
        return coin_list.index(target_coin)
    except ValueError:
        return "\"Tidak ditemukan\""

if __name__ == "__main__":
    import sys
    
    data = sys.stdin.read().splitlines()
    coin_list = list(map(int, data[0].strip('[]').split(','))) if data[0] != '[]' else []
    target_coin = int(data[1])
    
    print(find_coin_index(coin_list, target_coin))