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
iterationsarray = []
iterationsarray.insert(0,0)
functiongiter=[]
while function_evaluated!=0 and error > tolerance and contador < iterations :
            x_n = functiong_evaluated
            function_n = function_evaluated
            functiongiter.append(x_n)
            xaproximmate = x_n
            error=abs(x_n-functiongiter[contador])
            iterationsarray.append(contador)
            contador=contador+1


print iterations
print functiongiter
print iterationsarray
if function_evaluated==0:
    print "X_a es raiz"
elif error < tolerance:
    print str(xaproximmate)+ " es aproximacion con una tolerancia " +str(tolerance)+" hallado en la iteracion "+ str(contador) + " y un error de " +str(error)
else:
    print "El metodo fracaso en "+str(iterations)+" iteraciones"
plot.graficar(function)
