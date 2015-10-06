from astropy.table import Table
import parser

print "You're running the bisection method"
fx = raw_input('Enter a function: ')
xi = raw_input('Enter the lower limit ')
xi = float(xi)
xf = raw_input('Enter the upper limit ')
xf = float(xf)
tol = raw_input('Enter the tolerence ')
tol = float(tol)
iter = raw_input('Enter the maximum number of iterations ')
e = raw_input("If do you want to calculate the relative error write '1', else write anything ")
yi = parser.eval(fx,xi)
yf = parser.eval(fx,xf)
rows = []
if(yi*yf>0):
    print "The interval is not valid"
elif (yi==0):
    print "The lower limit "+str(xi)+" is a root"
elif (yf==0):
    print "The lower limit "+str(xf)+" is a root"
else:
    error = tol*2
    con = 1
    ym = 1
    xm = (xi+xf)/2
    while(ym!=0 and error>tol and con<=int(iter)):
        if(con>1):
            xm = nxm
        ym = float(parser.eval(fx,xm))
        xxi = xi
        xxf = xf
        if(ym*yi>0):
            xi = xm
            yi = ym
        else:
            xf = xm
            yf = ym
        nxm = float((xi+xf)/2)
        if(e==1):
            error = abs((nxm-xm)/nxm)
        else:
            error = abs(nxm-xm)
        v = (con,xxi,xxf,xm,ym,error)
        rows.append(v)
        con += 1
    t = Table(rows=rows, names=('iter', 'xi', 'xf', 'xm','f(xm)','error'))
    print(t)
    print("")
    if(ym == 0):
        print str(xm)+" is a root with a error of " + str(error)
    elif(error<tol):
        print str(xm)+" is a root with a error of " + str(error)
        print "The method has stoped because the error is < tolerance"
    else:
        print "the method has exceeded the number maximum of iterations"

