# coding=utf-8
__author__ = 'parzival'
import parser
import plot
from astropy.table import Table
tolerance=float(input("Type the tolerance "))
xaproximmate=float(input("Type the initial approximation "))
iterations=(input("Type the number of iterations "))
function=raw_input("Type the f function ")
functiong=raw_input("Type the g function \n")
function_evaluated=float(parser.eval(function,xaproximmate))
functiong_evaluated=float(parser.eval(functiong,xaproximmate))
error=tolerance+1
contador=(0)

rows=[]
while function_evaluated!=0 and error > tolerance and contador < iterations :
            x_n          = functiong_evaluated
            x_n_evaluated= float(parser.eval(functiong,x_n))
            xaproximmate = x_n
            error        = abs(x_n_evaluated-x_n)
            f_x_n_evaluated= float(parser.eval(function,x_n_evaluated))
            v=(contador,x_n,f_x_n_evaluated,error)
            rows.append(v)
            contador     = contador+1
            functiong_evaluated    = x_n_evaluated
            t = Table(rows=rows, names=('iter', 'x_n', 'f_x_n','error'))


if function_evaluated==0:
    print "X_a es raiz"
elif error < tolerance:
    print str(xaproximmate)+ " es aproximacion con una tolerancia " +str(tolerance)+" hallado en la iteracion "+ str(contador) + " y un error de " +str(error)
else:
    print "El metodo fracaso en "+str(iterations)+" iteraciones"

print t
plot.graficar(function)