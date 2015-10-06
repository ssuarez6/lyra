# coding=utf-8
__author__ = 'parzival'
import parser
import plot
from astropy.table import Table
tolerance=float(input("Type the tolerance "))
xaproximmate=float(input("Type the initial approximation "))
iterations=(input("Type the number of iterations "))
function=raw_input("Type the f function ")
functiong=raw_input("Type the g function ")
function_evaluated=float(parser.eval(function,xaproximmate))
functiong_evaluated=float(parser.eval(functiong,xaproximmate))
error=tolerance+1
contador=(0)

while function_evaluated!=0 and error > tolerance and contador < iterations :
            x_n          = functiong_evaluated
            x_n_evaluated= float(parser.eval(functiong,x_n))
            f_x_n        = float(parser.eval(function, functiong_evaluated))
            xaproximmate = x_n
            error        = abs(x_n_evaluated-x_n)
            contador     = contador+1
            functiong_evaluated    = x_n_evaluated
print iterations
if function_evaluated==0:
    print "X_a es raiz"
elif error < tolerance:
    print str(xaproximmate)+ " es aproximacion con una tolerancia " +str(tolerance)+" hallado en la iteracion "+ str(contador) + " y un error de " +str(error)
else:
    print "El metodo fracaso en "+str(iterations)+" iteraciones"
plot.graficar(function)
