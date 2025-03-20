def binary_search(arr, target, left=0, right=None, ascending=True):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return "Tidak ditemukan"
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    if ascending:
        if arr[mid] < target:
            return binary_search(arr, target, mid + 1, right, ascending)
        else:
            return binary_search(arr, target, left, mid - 1, ascending)
    else:
        if arr[mid] < target:
            # Untuk list descending, nilai yang lebih besar (dan target) ada di kiri
            return binary_search(arr, target, left, mid - 1, ascending)
        else:
            return binary_search(arr, target, mid + 1, right, ascending)

data = input().strip()
if data == "[]":
    arr = []
else:
    arr = list(map(int, data.strip("[]").split(',')))

target = int(input())

# Tentukan urutan list (ascending atau descending)
if len(arr) <= 1:
    ascending = True  # jika hanya ada 0 atau 1 elemen, tidak masalah
else:
    ascending = True if arr[0] < arr[-1] else False

result = binary_search(arr, target, 0, None, ascending)

# Jika hasil berupa string, tampilkan dengan tanda petik ganda
if isinstance(result, str):
    print(f"\"{result}\"")
else:
    print(result)