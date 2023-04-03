# your code goes here
def dfs(adj, visited, u):
    visited[u] = True
    for v in range(len(adj)):
        if adj[u][v] == 1 and not visited[v]:
            dfs(adj, visited, v)

t = int(input())
for i in range(t):
    n = int(input())
    adj = []
    for j in range(n):
        row = list(map(int, input().split()))
        adj.append(row)
    visited = [False] * n
    dfs(adj, visited, 0)
    if False in visited:
        print("Not connected")
    else:
        print("Connected")
