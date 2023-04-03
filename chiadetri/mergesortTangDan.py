# your code goes here
#Đệ quy. Sắp xếp trộn (MergeSort) tăng dần
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Chia dãy thành 2 nửa
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Sắp xếp các nửa dãy này đệ quy
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Trộn 2 nửa dãy đã được sắp xếp lại với nhau
    return merge(left, right)
    
    
def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result
n = int(input())
arr = list(map(int, input().split()))

arr = merge_sort(arr)

print(' '.join(map(str, arr)))
