def binary_search(arr, target, find_first):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            if find_first:
                right = mid - 1 
            else:
                left = mid + 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_FirstLast(arr, target):
    first = binary_search(arr, target, True)
    last = binary_search(arr, target, False)
    return [first, last]

arr = list(map(int, input().split()))
target = int(input())
print(find_FirstLast(arr, target))