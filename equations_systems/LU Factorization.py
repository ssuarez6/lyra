__author__ = 'parzival'
#from methods import eval
import scipy
import scipy.linalg
def PLU(A,):
	P, L, U = scipy.linalg.lu(A)
	return{'status': "SUCESS", 'message':"l"+str(L)+"u"+str(U)+"p"+str(P)}

