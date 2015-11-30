# This method recieves two arrays, one of the X's and other one of the Y's
# This prints the rects that result from generating an interpolating polynomial
# with a linear spline
	
def lin_spline(xs, ys):
	n = len(xs)
	m = []
	b = []
	for i in range(0, n-1):
		tmp = (ys[i]- ys[i+1]) / (xs[i] - xs[i+1])
		m.append(tmp)
		b.append(ys[i] - m[i]*xs[i])
	xi = xs[0:n-1]
	Xs = xs[1:]
	print len(xi) == len(Xs)
	for i in range(0, n-1):
		print "\nFor interval (%f, %f) the function is: \n\n" % (xi[i], Xs[i])
		print "f(x) = %f * x" % m[i]
		if b[i] >= 0:
			print "+ %f\n" % b[i]
		else:
			print "- %f\n" % -b[i]


if __name__=='__main__':
	xs = [2.3, 4.5, 6.2, 7.5]
	ys = [4.5, 6.3, 8.7, 9.4]
	print "Equises: "
	print xs
	print "Yeses: "
	print ys
	lin_spline(xs, ys)
