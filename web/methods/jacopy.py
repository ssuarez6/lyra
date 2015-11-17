from methods import eval
import numpy as np
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
    solutionVector=np.zeros(1,nEquations)
    #Ciclo que llena la columna solución
    for k in range(nEquations):
        for l in range(solutionColumns):
            solutionVector[k][l]  = input("Type the solution for equation "+str(k+1)+" "+"\n")

    return solutionVector


A=leeMat(input("Type the number of terms \n "),input("Type the number of equations in your system  \n"))
b=leeSol(input("Type the number of solutions in your system"))
filas=A.shape[0]
columnas=A.shape[1]

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(n):
        x = (b - np.dot(R,x))/ D
    return x


jacobi(A,b,)

