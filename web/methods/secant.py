from methods import eval
def method(tolerance,inferior_limit,superior_limit,iterations,function,e):
    function_0=float(eval(function,inferior_limit))
    function_1=float(eval(function,superior_limit))
    if(function_0==0):
        return {'status': "FAIL", 'message': "The lower limit "+str(inferior_limit)+" is a root"}
    else:
        counter=0
        den=function_1-function_0
        error=tolerance+1
        errors=[]
        xns = []
        function1s = []
        while error>tolerance and function_1!=0 and den!=0 and counter < iterations:
            x_n= superior_limit-function_1*((superior_limit-inferior_limit)/den)
            if(e==1):
                error=abs((x_n-superior_limit)/x_n)
            else:
                error=abs(x_n-superior_limit)
            inferior_limit=superior_limit
            function_0=function_1
            superior_limit=x_n
            function_1=eval(function,superior_limit)
            den=function_1-function_0
            errors.append(error)
            xns.append(x_n)
            function1s.append(function_1)
            counter=counter+1
    table = {'iter': counter-1, 'xi' : inferior_limit, 'xf': superior_limit, 'xn':xns,'error':errors}
    if (function_1 == 0):
        return {'status': "SUCESS", 'message': str(superior_limit) + " is a root with a error of " + str(error),
                'xn': x_n,
                'error': error, 'table': table, 'stopBy': 'xm'}
    elif (error < tolerance):
        return {'status': "SUCESS", 'message': str(x_n) + " is a root with a error of " + str(error), 'xn': x_n,
                'error': error, 'table': table, 'stopBy': 'tol'}
    elif (den==0):
        return {'status': "FAIL", 'message':'There is a possible multiple root',
                'error':error,'table':table, 'stopBy':'derivate'}
    else:
        return {'status': "SUCESS", 'message': str(x_n) + " is a possible root with a error of " + str(error),
                'x_n': x_n,
                'error': error, 'table': table, 'stopBy': 'iter'}
    
