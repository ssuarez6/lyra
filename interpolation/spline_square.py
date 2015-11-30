def square_spline(X, Y):
	n = len(X)
	a = []
	b = []
	c = []
	Mat = [ [0 for j in range(3*n+1) ] for i in range(3*n)  ]
	cont = 0
	# Fill f values
	for i in range(0, 2*(n-2)+1, 2): # Check this later on
		for j in [0,1,2]:
			Mat[i][cont*3+j] = X[cont+1] ** (3-j)
			Mat[i+1][cont*3+j] = X[cont+2] ** (3-j) #only God knows why this is here
		Mat[i][3*n+1] = Y[cont+1]
		Mat[i+1][3*n+1] = Y[cont+2]
		cont += 1
		
	cont = 0
	# Fill f' values
	for i in range(2*n, 3*n-2): #IMPORTANT: check later
		Mat[i, cont*3+1] = 2 * X[cont+2] #All these to check....
		Mat[i, cont*3+2] = 1
		Mat[i, cont*3+4] = - 2 * X[cont+2]
		Mat[i, cont*3+5] = -1
		cont += 1

	#Fill f'' values
	Mat[3*n-1][0] = 2
	printMat(Mat, 3*n)
	#Results
	R = gauss_elim_tot(Mat[0:3*n-1][0:], Mat[0:3*n+1][0:])
	cont = 0
	for i in range(n):
		a.append(R[3*cont])
		b.append(R[3*cont+1])
		c.append(R[3*cont+2])
		cont += 1
	printEq(a,b,c,X)

def printMat(M, n):
	print "The matrix is: "
	for i in range(n):
		_str = ""
		for j in range(n+1):
			_str += "%6.2f " % M[i][j]
		print ""

def printEq(a,b,c,X):
	m = len(X)
	Xi = X[0:m-2]
	Xs = X[1:m-1]
	n = len(a)
	for i in range(n)
		print "\nFor the (%f, %f) interval the function is: \n\n" % (Xi[i],Xs[i])
		print "Y = %.2f * x^2 + %.2f * x + %.2f\n" % (a[i], b[i], c[i])

def gauss_elim_tot(A, b):
	n = len(A)
	marks = range(n)
	for k in range(n-2):
		list_returned = total_pivot(A, b, marks, k)
		A = list_returned[0]
		b = list_returned[1]
		marks = list_returned[2]
		for i in range(k+1, n): #CHECK THIS LATER
			 #HELPMEPLEASEEEEEEEEEEEEEEEEEEE
			#Warning: Programmer about to commit suicide.
			#..
			#...
			#....
			#...
			#..
			#Danger: Too late
