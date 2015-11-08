from methods import eval

def method(fn,fn_p,fn_p_p, x0,tol,iter, e):
    abs_error = False
    if e is not '1':
        abs_error = True
    y = eval(fn, x0)
    error = tol + 1
    cont = 0
    xns =  []
    errors = []
    ys = []
    while y != 0 and error > tol and cont < iter:
        y = eval(fn, x0)
        y_prime = eval(fn_p, x0)
        y_p_p = eval(fn_p_p, x0)
        xn = x0 - (y*y_prime)/((y_prime*y_prime) - y*y_p_p)
        if abs_error:
            error = abs(xn-x0)
        else:
            error = abs((xn-x0)/xn)
        x0 = xn
        xns.append(xn)
        ys.append(y)
        errors.append(error)
        v = (cont,xn,y,error)
        cont = cont+1
    table = {'iter': cont-1, 'xn' : xns, 'ys': y, 'error':errors}

    if(y == 0):
        return {'status': "SUCESS", 'message': str(x0)+" is a root with a error of " + str(error), 'x0' : x0,
                    'error':error,'table':table, 'stopBy':'xm'}
    elif(error<tol):
        return {'status': "SUCESS", 'message': str(x0)+" is a root with a error of " + str(error), 'x0' : x0,
                'error':error, 'table':table, 'stopBy':'tol'}
    else:
        return {'status': "SUCESS", 'message': str(x0)+" is a possible root with a error of " + str(error), 'xm' : x0,
                'error':error, 'table':table, 'stopBy':'iter'}
