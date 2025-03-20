def find_fake_coin(coins, left, right):
    # Basis: jika hanya ada 1 koin, itulah koin palsu.
    if left == right:
        return left

    count = right - left + 1

    # Jika hanya ada 2 koin, kembalikan indeks koin yang lebih ringan.
    if count == 2:
        return left if coins[left] < coins[right] else right

    # Jika jumlah koin genap, bagi menjadi dua bagian sama besar.
    if count % 2 == 0:
        mid = left + count // 2 - 1
        left_sum = sum(coins[left:mid+1])
        right_sum = sum(coins[mid+1:right+1])
        if left_sum < right_sum:
            return find_fake_coin(coins, left, mid)
        else:
            return find_fake_coin(coins, mid+1, right)
    else:
        # Jika jumlah koin ganjil, kita bagi menjadi dua grup sama besar dan 1 koin sisaan.
        group_size = count // 2  # Ukuran tiap grup (floor division)
        left_sum = sum(coins[left:left+group_size])
        right_sum = sum(coins[left+group_size:left+group_size*2])
        if left_sum == right_sum:
            # Jika kedua grup seimbang, koin sisaan adalah palsu.
            return left + group_size * 2
        elif left_sum < right_sum:
            return find_fake_coin(coins, left, left + group_size - 1)
        else:
            return find_fake_coin(coins, left + group_size, left + group_size * 2 - 1)

n = int(input())
coins = list(map(int, input().split()))
print(find_fake_coin(coins, 0, n - 1))