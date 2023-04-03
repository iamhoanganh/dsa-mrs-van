# your code goes here
t = int(input())

def DFS(point,checkV):
	checkV[point]=0
	for i in range(0,n):
		if (a[point][i]==1) and (checkV[i] == 1) and (i!=point):
			checkV[i]=0
			res.append(i)
			DFS(i,checkV)

def checkHuong():
    check = 0
    for i in range(0,n):
        for j in range(i,n):
            if (a[i][j]!=a[j][i] and check ==0):
                return 1
    print(check)
    return check

		
    
    
for i in range (0,t):
	a = []
	
	n = int(input())
	
	for i in range(0, n):
	    a.append([int(x) for x in input().split()])
	check = 0
	
	for i in range(0,n):
		res =[]
		Visited = [1 for x in range (n)]
		DFS(i,Visited)
		res.sort()
		if sum(Visited)!=0:
			print("Not connected")
			break
		elif (i==n-1):
			if checkHuong()==1:
			    print("Strongly Connected")
			else: print("Weakly Connected")