# -*- coding: utf-8 -*-
__author__ = 'parzival'
import numpy as np
from tabulate import tabulate

from astropy.table import Table
def inputmatrix():

    numberofColumns = input("Type the number of terms \n ")#  Le pide al usuario el
                                                           #  numero de incognitas que tiene el sistema


    numberofRows    = input("Type the number of equations in your system  \n")  # Le pide al usuario el numero
                                                                                # de ecuaciones
    ax              = np.zeros((numberofRows,numberofColumns)) #Creo una matriz del tamaño que ingreso el usuario
                                                               # y la lleno de zeros
    solutionColumns = 1                                        # Numero de columnas que tiene la matriz solucion
    solutionVector  = np.zeros((numberofRows,solutionColumns)) # Matriz solucion de tamaño Numero de ecuaciones*1

    #Ciclo que llena la matriz
    for i in range(numberofRows):
        for j in range(numberofColumns):
            ax[i][j]   = input("Type the term number "+ str(j+1)+ " in the equation number "+ str(i+1)+ " "+"\n")

    #Ciclo que llena la columna solución
    for k in range(numberofRows):
        for l in range(solutionColumns):
            solutionVector[k][l]  = input("Type the solution for equation "+str(k+1)+" "+"\n")

    #Añado a la matriz la columna solución
    ax = np.c_[ax,solutionVector]
    terminos=[]
    for n in range(numberofRows):
        terminos.append("x"+str(n+1))
    terminos.append("R.H.S")
    #terminos.append("Solution")
    t= tabulate(ax,tablefmt="fancy_grid",headers=terminos[0:numberofRows+1])
    return t

matriz=inputmatrix()
print matriz


