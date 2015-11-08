from methods import eval

def method(function, iterations, tolerance, e, functiong, xaproximmate):
    function_evaluated=float(eval(function,xaproximmate))
    functiong_evaluated=float(eval(functiong,xaproximmate))
    error=tolerance+1
    contador=(0)
    errors =[]
    xns = []
    fxns = []
    while function_evaluated!=0 and error > tolerance and contador < iterations :
        x_n          = functiong_evaluated
        x_n_evaluated= float(eval(functiong,x_n))
        if(e==1):
            error = abs((x_n_evaluated-x_n)/x_n_evaluated)
        else:
            error = abs(x_n_evaluated-x_n)
        f_x_n_evaluated= float(eval(function,x_n_evaluated))
        fxns.append(f_x_n_evaluated)
        xns.append(x_n)
        errors.append(error)
        contador     = contador+1
        functiong_evaluated    = x_n_evaluated
    table = {'iter': contador-1, 'ym' : fxns, 'error':errors}
    if(f_x_n_evaluated == 0):
        return {'status': "SUCESS", 'message': str(x_n)+" is a root with a error of " + str(error), 'xn' : x_n,
                    'error':error, 'table':table, 'stopBy':'xm'}
    elif(error<tolerance):
        return {'status': "SUCESS", 'message': str(x_n)+" is a root with a error of " + str(error), 'xn' : x_n,
                'error':error, 'table':table, 'stopBy':'tol'}
    else:
        return {'status': "SUCESS", 'message': str(x_n)+" is a root with a error of " + str(error), 'xm' : x_n,
                'error':error, 'table':table, 'stopBy':'iter'}