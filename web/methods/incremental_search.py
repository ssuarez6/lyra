from methods import eval

def method(fx,delta,xi):
    yis = []
    yyis = []
    xi = float(xi)
    delta = float(delta)
    yi = eval(fx,xi)
    yis.append(yi)
    xxi = xi+ delta
    yyi = eval(fx,xxi)
    yyis.append(yyi)
    c=0
    while(int(yi*yyi)>0):
        xi = xi+delta
        yi = eval(fx,xi)
        yis.append(yi)
        xxi = xi+ delta
        yyi = eval(fx,xxi)
        yyis.append(yyi)
        c += 1
        if c<=10:
            print str(xi) + "\n"
    yis.append(yyis[len(yyis)-1])
    return {'status': 'SUCCES', 'messaje':'There is a root in the interval ['+
            str(xi)+ ' , '+str(xxi)+']', 'xi':str(xi), 'xf':str(xxi), 'list':yis }
