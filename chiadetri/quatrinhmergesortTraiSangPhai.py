# your code goes here
n = int(input())
s = input()
arr = [int(_) for _ in s.split()]
print(s)
def mergeSort(l, r):
    if len(arr[l:r+1]) > 1:
        m = int((l + r) / 2)
        print(f'Divide: {l} --> {m} and {m+1} --> {r}')
        print(" ".join([str(x) for x in arr[l:m+1]]),"::", " ".join([str(x) for x in arr[m+1:r+1]]))
        mergeSort(l, m)
        mergeSort(m+1, r)
        temp = [None for x in range(l, r+1)]
        k = 0
        i = l
        j = m+1
        print(f'Merge: {l} --> {m} and {m+1} --> {r}')
        while i < m+1 and j < r+1:
            if arr[i] < arr[j]:
                temp[k] = arr[i]
                i+=1
            else:
                temp[k] = arr[j]
                j+=1
            k+=1
        while i<m+1:
            temp[k] = arr[i]
            i+=1
            k+=1
        while j<r+1:
            temp[k] = arr[j]
            j+=1
            k+=1
        print(" ".join([str(x) for x in temp]), end="\n\n")
        arr[l: r+1] = temp

mergeSort(0, n-1)