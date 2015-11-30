__author__ = 'parzival'
#from methods import eval
from tabulate import tabulate
import numpy as np
import scipy
import scipy.linalg
def leeMat(numberofColumns, numberofRows):
    ax=np.zeros((numberofRows,numberofColumns)) #Creo una matriz del size que ingreso el usuario
                                                               # y la lleno de zeros
    #Ciclo que llena la matriz
    for i in range(numberofRows):
        for j in range(numberofColumns):
            ax[i][j]= input("Type the term number "+ str(j+1)+ " in the equation number "+ str(i+1)+ " "+"\n")
    A={'matriz':ax}
    return ax

def leeSol(nEquations):
    solutionColumns=1
    solutionVector= np.zeros((1, nEquations))
    for k in range(nEquations):
        for l in range(solutionColumns):
            solutionVector[k][l]  = input("Type the solution for equation "+str(k+1)+" "+"\n")

    B={'solucion':solutionVector}
    return solutionVector



A=leeMat(input("Type the number of terms in your system \n "),input("Type the number of equations in your system \n"))
B=leeSol(input("Type the number of equations in your system "))
#B=[20,18,31,12]
print "Matriz A"
print A
#print tabulate(A.get('matriz'), tablefmt="fancy_grid")
print "Matriz B"
print B
P, L, U = scipy.linalg.lu(A.get('matriz'))
cholesky= np.linalg.cholesky(P)
solution= scipy.linalg.solve(A.get('matriz') ,B)
print "Matriz P"
print P
#print tabulate(P, tablefmt="fancy_grid")
print "Matriz L"
print L
#print tabulate(L, tablefmt="fancy_grid")
print "Matriz U"
print U
#print tabulate(U, tablefmt="fancy_grid")
print "Cholesky"
print cholesky
print "Sustitucion Regresiva"
print solution
print "Sustitucion en L"
print scipy.linalg.solve(L,B)
print "Sustitucion en U"
print scipy.linalg.solve(U,B)