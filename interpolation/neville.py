def nev_int(points, value, xs, ys):
	res = ""
	table = [[ys[i] for i in range(0, points)] for j in range(0, points)]
	for i in range(0, points):
		for j in range(1, i+1):
			table[i][j] = ((value-xs[i-j])*table[i][j-1] - ((value-xs[i])*table[i-1][j-1]))/ (xs[i]-xs[i-j])
	res += "Value: " + str(table[points-1][points-1])
	
