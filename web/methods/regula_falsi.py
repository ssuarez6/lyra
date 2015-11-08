from methods import eval

def method(fx,xi,xf,tol,iter,e = 000):
    xi = float(xi)
    xf = float(xf)
    tol = float(tol)
    yi = eval(fx,xi)
    yf = eval(fx,xf)
    xis = []
    xfs = []
    xms = []
    yms = []
    errors = []
    if(yi*yf>0):
        return {'status': "FAIL", 'message': "The interval is not valid"}
    elif (yi==0):
        return {'status': "FAIL", 'message': "The lower limit "+str(xi)+" is a root"}
    elif (yf==0):
        return {'status': "FAIL", 'message': "The lower limit "+str(xf)+" is a root"}
    else:
        error = tol*2
        con = 1
        ym = 1
        xm = (xi+xf)/2
        while(ym!=0 and error>tol and con<=int(iter)):
            if(con>1):
                xm = nxm
            ym = float(eval(fx,xm))
            xxi = xi
            xxf = xf
            if(ym*yi>0):
                xi = xm
            else:
                xf = xm
            nxm = xi-((yi*(xi-xf))/(yi-yf))
            if(e==1):
                error = abs((nxm-xm)/nxm)
            else:
                error = abs(nxm-xm)
            xis.append(xxi)
            xfs.append(xxf)
            xms.append(xm)
            yms.append(ym)
            errors.append(error)
            con += 1
        table = {'iter': con-1, 'xi' : xis, 'xf': xfs, 'ym':yms,'error':errors}
        if(ym == 0):
            return {'status': "SUCESS", 'message': str(xm)+" is a root with a error of " + str(error), 'xm' : xm,
                    'error':error, 'iter':con-1, 'table':table, 'stopBy':'xm'}
        elif(error<tol):
            return {'status': "SUCESS", 'message': str(xm)+" is a root with a error of " + str(error), 'xm' : xm,
                    'error':error, 'iter':con-1, 'table':table, 'stopBy':'tol'}
        else:
            return {'status': "SUCESS", 'message': str(xm)+" is a root with a error of " + str(error), 'xm' : xm,
                    'error':error, 'iter':iter, 'table':table, 'stopBy':'iter'}