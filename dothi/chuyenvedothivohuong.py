# your code goes here
t = int(input()) # amount of test case
for _ in range(t):
    n = int(input()) # amount of vertex
    adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                adj_matrix[j][i] = 1
    
    for i in range(n):
        for j in range(n):
            print(adj_matrix[i][j], end=" ")
        print()
                    