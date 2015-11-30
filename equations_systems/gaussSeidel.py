import numpy as np
def gauss(A, b, x, n, tol, l ):
	it_count = 0
	error = tol+1
	while it_count<n:
		print "Current solution", x
		print "Current error", error
		x_new = no.zeros_like(x)
		i = 0
		for i in range(A.shape[0]):
			s1 = np.dot(A[i, :i], x_new[:i])
			s2 = np.dot(A[i, i+1:], x[i+1:])
			x_new[i] = np.divide((b[i]-s1-s2), A[i, i])*l + (1-l)*x[i]
		error = np.amax(np.dot(A, x)-b)
		x = x_new
		it_count += 1
	print "Solution: "
	print x

