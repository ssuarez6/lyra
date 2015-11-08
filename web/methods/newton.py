from methods import eval

def method(tolerance,xapproximate,iterations,function,derivative_function,e):
    function_evaluated=float(eval(function,xapproximate))
    derivative_evaluated= float(eval(derivative_function,xapproximate))
    counter=0
    error=tolerance+1
    xns=[]
    errors = []
    fns = []
    dfns = []
    while error>tolerance and function_evaluated!=0 and derivative_function!=0 and counter<iterations:
        x_n = xapproximate-(function_evaluated/derivative_evaluated)
        f_n=float(eval(function,x_n))
        d_f_n=float(eval(derivative_function,x_n))
        function_evaluated=f_n
        derivative_evaluated=d_f_n
        if(e==1):
            error=abs((x_n-xapproximate)/x_n)
        else:
            error=abs(x_n-xapproximate)
        xapproximate=x_n
        errors.append(error)
        xns.append(x_n)
        fns.append(f_n)
        dfns.append(d_f_n)
        counter=counter+1
    table = {'iter': counter-1, 'xns' : xns, 'fns': fns, 'dfns':dfns,'error':errors}

    if(function_evaluated == 0):
        return {'status': "SUCESS", 'message': str(xapproximate)+" is a root with a error of " + str(error), 'xn' : xapproximate,
                'error':error,'table':table, 'stopBy':'xm'}
    elif(error<tolerance):
        return {'status': "SUCESS", 'message': str(xapproximate)+" is a root with a error of " + str(error), 'xn' : xapproximate,
                'error':error, 'table':table, 'stopBy':'tol'}
    elif(derivative_evaluated==0):
        return {'status': "FAIL", 'message': str(xapproximate)+" is a root with a possible multiple root", 'xn' : xapproximate,
                'error':error,'table':table, 'stopBy':'derivate'}
    else:
        return {'status': "SUCESS", 'message': str(xapproximate)+" is a possible root with a error of " + str(error), 'xn' : xapproximate,
                'error':error, 'table':table, 'stopBy':'iter'}