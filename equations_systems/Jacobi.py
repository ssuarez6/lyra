import numpy as np
from numpy import array, zeros, diag, diagflat, dot

#tol=input("Digite la tolerancia \n")
#niter=input("Digite el numero de iteraciones \n")
contador=0
#dispersion=tol+1
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
    solutionVector=np.zeros((solutionColumns,nEquations))
    #Ciclo que llena la columna solucion
    for k in range(nEquations):
        for l in range(solutionColumns):
            solutionVector[k][l]  = input("Type the solution for equation "+str(k+1)+" "+"\n")

    return solutionVector



A=leeMat(input("Type the number of terms \n "),input("Type the number of equations in your system  \n"))

x=initialValues(input("Type the initial values \n"))
n=input("Type the number of iterations")


def jacobi(A,b,n,x):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x




print "all good"
