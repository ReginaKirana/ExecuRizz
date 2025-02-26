# Difficulty level : Easy
# Number           : 9
# Title            : SPBU Natlan
# ---------------------------------------------------------------------------------

# Diberikan dua array gas dan cost, masing-masing berisi n elemen, 
# di mana gas[i] menunjukkan jumlah bahan bakar yang tersedia di stasiun ke-i, 
# dan cost[i] menunjukkan bahan bakar yang dibutuhkan untuk mencapai stasiun berikutnya. 
# Anda harus menentukan indeks stasiun awal (0-based) dari mana-
# seseorang dapat memulai perjalanan mengelilingi seluruh sirkuit satu kali-
# tanpa kehabisan bahan bakar. 
# Jika perjalanan memungkinkan, kembalikan indeks stasiun awal tersebut; jika tidak, kembalikan -1. 
# Diasumsikan bahwa hanya ada satu solusi unik jika perjalanan dapat diselesaikan.

# ---------------------------------------------------------------------------------
def can_complete_circuit(gas, cost):
    total_tank, current_tank, start_index = 0, 0, 0
    
    for i in range(len(gas)):
        balance = gas[i] - cost[i]
        total_tank += balance
        current_tank += balance
        
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0
    
    return start_index if total_tank >= 0 else -1

# Membaca input dan memprosesnya
gas = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = can_complete_circuit(gas, cost)
print(result)