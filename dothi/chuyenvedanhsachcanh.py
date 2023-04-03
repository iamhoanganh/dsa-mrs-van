# your code goes here
t = int(input()) # amount of test case
for _ in range(t):
    n = int(input()) # amount of vertex
    adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    edge_list = []
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                edge_list.append((i, j))
    print(", ".join([f"({u}, {v})" for u, v in edge_list]))
    print()