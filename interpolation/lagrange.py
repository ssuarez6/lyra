def lag_int(points, value, xs, ys):
	pol = "P(x) = "
	result = 0.0
	for k in range(0, points):
		productory = 1
		term = ""
		for i in range(0, points):
			if i!=k:
				productory *= ((value-xs[i])/(xs[k]-xs[i]))
				term += "[(x-"+str(xs[i])+")/("+str(xs[k])+"-"+str(xs[i])+")]"
		if ys[k]>0:
			pol += "+"
		pol += str(ys[k])+"*"+term+"\n"
		result += productory * ys[k]
	pol = "Lagrange interpolating polynomial: " + pol +"\n value: " + str(result)
	return pol
