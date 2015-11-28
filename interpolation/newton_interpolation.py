def newton_int(points, value, xs, ys):
	res = ""
	table = [[ys[i] for i in range(0, points)] for j in range(0, points)]
	for i in range(0, points):
		for j in range(0, i+1):
			table[i][j] = (table[i][j-1] - table[i-1][j-1]) / (xs[i-j])

	pol = "P(x): " + str(table[0][0])
	tmp = ""
	result = table[0][0]
	aux = 1
	for i in range(0, points):
		tmp += "(x-"+str(xs[i-1])+")"
		pol += "\n"+("+" if table[i][i]>0 else "")+str(table[i][i])+"*"+str(tmp)
		aux *= value-xs[i-1]
		result += table[i][i]*aux
	return "Newton interpolating polynomial: " + pol + "value: " + result
