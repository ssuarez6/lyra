from tabulate import tabulate
import numpy as np
def readMat(cols, rows):
    M = []
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(input("Type the term number " + str(j+1)+" in the equation number "+str(i+1)+"\n=>"))
        M.append(tmp)
    return M

def aumented_mat(A,b):
    M = np.c_[A,b]
    return M

def pivot(Matrix):
#    p = 'x'
    p = raw_input("Select your pivot technique:\n|:partial(p)\n|:total(t)\n|:escaloned(e)\n===>")
    if p == 'p':
        return partial_pivot(Matrix)
    elif p == 't':
        return total_pivot(Matrix)
    elif p == 'e':
        return escaloned_pivot(Matrix)
    else:
        pivot(Matrix)

def partial_pivot(Matrix):
    maj = Matrix[0][0]
    row_max = 0
    for row in range(len(Matrix)):
        if Matrix[row][0] > maj:
            row_max = row
            maj = Matrix[row][0]
    tmp = [x for x in Matrix[0]]
    Matrix[0] = Matrix[row_max]
    Matrix[row_max] = tmp
    return Matrix


def total_pivot(M):
    maj = 0
    row_max = 0
    col_max = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > maj:
                row_max = i
                col_max = j
                maj = M[i][j]
    tmp = [x for x in M[0]]
    M[0] = M[row_max]
    M[row_max] = tmp
    print M
    for x in range(len(M)):
        tmp2 = M[x][0]
        M[x][0] = M[x][row_max]
        M[x][row_max] = tmp2
        print tmp2
    return M

def escaloned_pivot(M):
    pass

def gauss_elimin(Ab):
    for k in range(len(Ab)-2):
        for i in range(k+1, len(Ab)):
            m = Ab[i][k] / Ab[k][k]
            for j in range(k, len(ab)+1):
                Ab[i][j] = Ab[i][j] - m*Ab[k][j]
    return Ab

def regresive_sust(Ab):
    x = []
    for i in range(len(Ab)-1, -1, -1):
        _sum = 0
        for p in range(i+1, len(Ab)):
            _sum += 


cols = input("Type the number of x's \n-->")
rows = input("Type the number of equations\n-->")
A = readMat(cols, rows)
print "\n..::..::..::..::..::..::..::..::..\nNow Write the solution column\n"
b = readMat(1, rows)
A = pivot(A)
