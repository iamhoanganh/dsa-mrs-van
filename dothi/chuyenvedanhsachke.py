# your code goes here
t = int(input()) # amount of test case
for _ in range(t):
    n = int(input()) # amount of vertex
    adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    adj_list = [[] for _ in range(n)]  # Khởi tạo danh sách kề
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                adj_list[i].append(j)
                # print(f"({i}, {j})", end=", ")
    for vertex in range(n):
        print("Vertex   {}:  {canh}".format(vertex, canh= ',  '.join(map(str, adj_list[vertex]))))
    print()