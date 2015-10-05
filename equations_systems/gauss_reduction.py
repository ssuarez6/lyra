from decimal import *
def read_mat(n, m):
    X = []
    for i in range(n):
        Y = []
        for j in range(m):
            _str = "Insert element at " + str(i) +"," + str(j)
            print _str
            a = Decimal(raw_input())
            Y.append(a)
        X.append(Y)
    return X

def aug_mat(A, b):
    return

def gauss_elimination(Ab):
    return

def regresive_sust(Ab):
    return

if __name__ == "__main__":
    getcontext().prec = 8
    n = int(raw_input("Martix is N x M, insert N: "))
    m = int(raw_input("Insert M: "))
    A = read_mat(n,m)
    n = int(raw_input("Now dimensions for solution matrix, insert N: "))
    m = int(raw_input("Insert M: "))
    b = read_mat(n,m)
    Ab = aug_mat(A, b)
    Ab_prime = gauss_elimination(Ab)
    X = regresive_sust(Ab_prime)
