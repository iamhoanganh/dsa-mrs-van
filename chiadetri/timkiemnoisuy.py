# your code goes here
def interpolation_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right and arr[left] <= x <= arr[right]:
        pos = left + ((x - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1
    return -1

# Đọc dữ liệu vào từ input
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = [int(input()) for _ in range(m)]

# Sắp xếp mảng theo thứ tự tăng dần
arr.sort()

# In ra mảng đã sắp xếp
print(*arr)

# Tìm vị trí của các phần tử trong mảng đã sắp xếp
for x in queries:
    index = interpolation_search(arr, x)
    print(index if index != -1 else -1)
