__author__ = 'parzival'
import parser
import plot
from astropy.table import Table
tolerance=float(raw_input("Type the tolerance \n"))
xapproximate=float(raw_input("Type the initial approximation \n "))
iterations=input("Type the iterations \n ")
function=raw_input("Type the function \n ")
derivative_function=raw_input("Type the derivative of the function \n")
function_evaluated=float(parser.eval(function,xapproximate))
derivative_evaluated= float(parser.eval(derivative_function,xapproximate))
counter=0
error=tolerance+1
rows=[]
while error>tolerance and function_evaluated!=0 and derivative_function!=0 and counter<iterations:
    x_n = xapproximate-(function_evaluated/derivative_evaluated)
    f_n=float(parser.eval(function,x_n))
    d_f_n=float(parser.eval(derivative_function,x_n))
    function_evaluated=f_n
    derivative_evaluated=d_f_n
    error=abs(x_n-xapproximate)
    xapproximate=x_n
    v=(counter,x_n,f_n,d_f_n,error)
    rows.append(v)
    counter=counter+1
    t = Table(rows=rows, names=('iter', 'x_n', 'f_x_n','f_d_x_n','error'))
if function_evaluated==0:
    print str(xapproximate)+"is a root"
elif error<tolerance:
    str(x_n)+ "is an approximation to a root with a tolerance of"+str(tolerance)
elif derivative_evaluated==0:
    str(x_n)+ "is a posible multiple root"
else:
    "Fail after"+str(iterations)+"iteraciones"


print t
plot.graficar(function)