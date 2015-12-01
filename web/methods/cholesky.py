__author__ = 'parzival'
#from methods import eval
import scipy
import scipy.linalg

def cholesky(A):
    cholesky= np.linalg.cholesky(A)
    return{'status': "SUCESS", 'message':str(cholesky)}
