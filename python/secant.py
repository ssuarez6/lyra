__author__ = 'parzival'
import parser
import plot
from astropy.table import Table
tolerance=float(raw_input("Type the tolerance \n"))
inferior_limit=float(raw_input("Type the inferior limit \n"))
superior_limit=float(raw_input("Type the superior limit \n"))
iterations=input("Type the number of iterations \n")
function=raw_input("Type the function \n")
function_0=float(parser.eval(function,inferior_limit))
function_1=float(parser.eval(function,superior_limit))
if(function_0==0):
    print str(function_0)+"is a root"
else:
    counter=0
    den=function_1-function_0
    error=tolerance+1
    rows=[]
    while error>tolerance and function_1!=0 and den!=0 and counter < iterations:
        x_n= superior_limit-function_1*((superior_limit-inferior_limit)/den)
        error=abs(x_n-superior_limit)
        inferior_limit=superior_limit
        function_0=function_1
        superior_limit=x_n
        function_1=parser.eval(function,superior_limit)
        den=function_1-function_0
        v=(counter,x_n,function_1,error)
        rows.append(v)
        t = Table(rows=rows, names=('iter', 'x_n', 'f_x_n','error'))
        counter=counter+1
    if function_1==0:
        print str(superior_limit)+"is a root"
    elif error<tolerance:
        print str(superior_limit)+" is an approximation with a root of a tolerance "+str(tolerance)
    elif den==0:
        print "There is a possible multiple root"
    else:
        print "Fail after"+str(iterations)+"iterations"


print t
plot.graficar(function)

