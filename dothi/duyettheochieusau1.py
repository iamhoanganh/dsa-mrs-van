# your code goes here
t = int(input())

def DFS(point,checkV):
	checkV[point]=0
	for i in range(0,n):
		if (a[point][i]==1) and (checkV[i] == 1) and (i!=point):
			checkV[i]=0
			res.append(i)
			DFS(i,checkV)
			

for i in range (0,t):
	a = []
	n = int(input())
	
	for i in range(0, n):
	    a.append([int(x) for x in input().split()])

	for i in range(0,n):
		res =[]
		Visited = [1 for x in range (n+1)]
		DFS(i,Visited)
		res.sort()

		print("From{:4d} can visit: ".format(i),end="")
		if len(res)==0:
			print("No vertex")
		else:
			print ((','.join(['%3d']*len(res))) % tuple(res))