__author__ = 'OASIS'
import numpy as np
from scipy.linalg import solve
def leeMat(numberofColumns, numberofRows):
    ax=np.zeros((numberofRows,numberofColumns)) #Creo una matriz del size que ingreso el usuario
                                                               # y la lleno de zeros
    #Ciclo que llena la matriz
    for i in range(numberofRows):
        for j in range(numberofColumns):
            ax[i][j]= input("Type the term number "+ str(j+1)+ " in the equation number "+ str(i+1)+ " "+"\n")

    return ax

def leeSol(nEquations):
    solutionColumns=1
    solutionVector=np.zeros((1,nEquations))
    #Ciclo que llena la columna solucion
    for k in range(nEquations):
        for l in range(solutionColumns):
            solutionVector[k][l]  = input("Type the solution for equation "+str(k+1)+" "+"\n")

    return solutionVector

def initialValues(nEquations):
    initalValuesColumns=1
    initialValues=np.zeros((initalValuesColumns,nEquations))
    #Ciclo que llena la columna solucion
    for m in range(nEquations):
        for n in range(initalValuesColumns):
            initialValues[m][n]  = input("Type the solution for equation "+str(m+1)+" "+"\n")

    return initialValues

A=leeMat(input("Type the number of terms \n "),input("Type the number of equations in your system  \n"))
b=leeSol(input("Type the number of solutions in your system"))
x=initialValues(input("Type the initial values for the method"))
n=input("Type the number of iterations")

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print str(i).zfill(3),
        print(x)
    return x






print gauss(A, b, x, n)
print solve(A, b)