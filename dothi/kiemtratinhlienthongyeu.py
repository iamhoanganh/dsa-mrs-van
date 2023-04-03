# your code goes here
t = int(input())

def DFS(point,checkV):
	checkV[point]=0
	for i in range(0,n):
		# print("Check out: ",point, i,end=" - ")
		# print(checkV)
		if (a[point][i]==1) and (checkV[i] == 1) and (i!=point):
			# print(a[point][i])
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

def checkLienThong():
    for i in range(0,n):
        res =[]
        Visited = [1 for x in range (n)]
        DFS(i,Visited)
        res.sort()
        if sum(Visited)!=0:
            return 1
    return 0
    

def chuyenCothanhVo():
    for i in range(0,n):
        for j in range(i,n):
            if (a[i][j]!=a[j][i]):
                a[i][j] = a[j][i] = 1


for i in range (0,t):
	a = []
	res =[]
	n = int(input())
	
	for i in range(0, n):
	    a.append([int(x) for x in input().split()])
	check = 0
	if (checkLienThong() == 1):
	    chuyenCothanhVo()
	    if (checkLienThong()==1):
	        print("Not Connected At All")	#Không liên thông
	    else: print("Weakly Connected")		#Liên thông yếu = Vô hướng liên thông
	else: print("Strongly Connected")		#Liên thông mạnh = Liên thông ngay từ đầu