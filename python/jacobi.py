__author__ = 'parzival'
import numpy as np
from tabulate import tabulate
import scipy.linalg as la

from fractions import Fraction
from astropy.table import Table
numberofColumns= input("Type the number of terms \n ")#  Le pide al usuario el
                                                      #  numero de incognitas que tiene el sistema


numberofRows= input("Type the number of equations in your system  \n")  # Le pide al usuario el numero
                                                                        # de ecuaciones
def inputmatrix():

    ax= np.zeros((numberofRows,numberofColumns)) #Creo una matriz del tamao que ingreso el usuario                                                               # y la lleno de zeros

    #Ciclo que llena la matriz
    for i in range(numberofRows):
        for j in range(numberofColumns):
            ax[i][j] = Fraction(input("Type the term number "+ str(j+1)+ " in the equation number "+ str(i+1)+ " "+"\n"))
    return ax


matriz=np.array((inputmatrix()))


def solutionMatrix():
    solutionColumns = 1                                        # Numero de columnas que tiene la matriz solucion
    solutionVector  = np.zeros((numberofRows,solutionColumns)) # Matriz solucion de tamao Numero de ecuaciones*1
    #Ciclo que llena la columna solucion
    for k in range(numberofRows):
        for l in range(solutionColumns):
            solutionVector[k][l]  = Fraction(input("Type the solution for equation "+str(k+1)+" "+"\n"))
    return solutionVector
def valoresIniciales():
    valores=[]
    for m in range(numberofColumns):
        valores.append(input("Digite el vector de valores iniciales \n"))
    return valores


columnasolucion=np.array(solutionMatrix())
guess=valoresIniciales()
numberOfIterations=input("Digite el numero de iteraciones \n")

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)
    L=np.tril(A)
    U=A-L
    for i in range(n):
        x = np.linalg.inv(D)*(L+U)*x+np.linalg.inv(D)*b
        print str(i).zfill(3),
        #print(x)
    return x



def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    terminos=[]
    for k in range(numberofRows):
        terminos.append("x"+str(k+1))
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print str(i)+"\n"
        t= tabulate(np.transpose(x),tablefmt="fancy_grid",headers=terminos[0:numberofRows])


        print t
    return x

#solucionJacobi=jacobi(matriz,columnasolucion,guess,numberOfIterations)
solucionGauss=gauss(matriz,columnasolucion,guess,numberOfIterations)
ax=np.c_[matriz,columnasolucion]
terminos=[]
for n in range(numberofRows):
    terminos.append("x"+str(n+1))

terminos.append("Solution")

originalMatriz= tabulate(ax,tablefmt="fancy_grid",headers=terminos[0:numberofRows+1])


#print originalMatriz