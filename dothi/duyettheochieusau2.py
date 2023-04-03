# your code goes here
def dfs(visited, index, arr, n, parents):
    visited[index] = 1
    for i in range(n):
        if arr[index][i] == 1 and index != i and visited[i] == 0:
            parents[i] = index
            dfs(visited, i, arr, n, parents)

t = int(input())
for k in range(t):
    n, u, v = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    visited, parents = [0]*n, [-1]*n
    dfs(visited, u, arr, n, parents)
    
    print(f"Path from {u} to {v}:", end="")
    if visited[v] == 0:
        print(" No path exits")
    else:
        path = []
        tmp = v
        while u != tmp:
            path.append(tmp)
            tmp = parents[tmp]
        path.append(u)
        first = True
        for i in range(len(path)-1, -1, -1):
            if first:
                first = False
            else:
                print(" -->", end="")
            print(f" {path[i]}", end="")
        print()
