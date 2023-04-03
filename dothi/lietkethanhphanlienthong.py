# your code goes here
def dfs(visited, index, arr, n, vec):
    visited[index] = 1
    vec.append(index)
    for i in range(n):
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            dfs(visited, i, arr, n, vec)

t = int(input())
for k in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    count = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            vec = []
            count += 1
            dfs(visited, i, arr, n, vec)
            vec.sort()
            for j in range(len(vec)):
                print(vec[j], end=" ")
            print()
    print()
