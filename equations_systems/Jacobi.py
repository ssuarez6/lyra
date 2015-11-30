from __future__ import division
from numpy import array, zeros, diag, diagflat, dot
import numpy as np

"""Solves the equation Ax=b via the Jacobi iterative method."""
"""A: Coefficient, b: solution, n: iterations, x: initial values, tol: tolerance, l: lambda""" 
def jacobi(A,b,n,x,tol,l):
	it_count = 0
	error = tol+1
	while it_count<n:
		print "Current solution:", x
		print "Current error:", error
		x_new = np.zeros_like(x)
		i = 0
		for i in range(A.shape[0]):
			s1 = np.dot(A[i, :i], x[:i])
			s2 = np.dot(A[i, i + 1:], x[i + 1:])
			x_new[i] = np.divide((b[i]-s1-s2), A[i,i])*l + (1-l)*x[i]
		error = np.amax(np.dot(A,x) - b)	
		x = x_new
		it_count += 1
	print "Solution: "
	print x

if __name__ == '__main__':
	A = np.array([[10.0, -1.0, 2.0, 0.0], [-1.0,11.0,-1.0,3.0],[2.0,-1.0,10.0,-1.0],[0.0, 3.0, -1.0, 8.0]])
	b = np.array([6.0,25.0,-11.0,15.0])
	x0 = np.array([0.0,0.0,0.0,0.0])
	_iter = 10
	err = 1e-8
	l  = 1.0
	jacobi(A, b, _iter, x0, err, l)
