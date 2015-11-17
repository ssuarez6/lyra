from flask_restful import Resource, request
from app import api
from methods import bisection, regula_falsi, fixed_point, \
    multiple_root, newton, secant, incremental_search


class RootMethods(Resource):

    def post(self):
        fx = request.form['fx']
        xi = request.form['xi']
        method = request.form['method']
        r = None

        if(method!='incremental'):
            tol= request.form['tol']
            iter = request.form['iter']
            e = request.form['e']
        else:
            delta = request.form['delta']
            return incremental_search.method(fx,delta,xi)

        if(method == 'bisection'):
            xf = request.form['xf']
            r = bisection.method(fx,xi,xf,tol,iter,e)
        elif(method=='regula_falsi'):
            xf = request.form['xf']
            r = regula_falsi.method(fx,xi,xf,tol,iter,e)
        elif(method=='fixed_point'):
            fg = request.form['fg']
            r = fixed_point.method(fx,iter,tol,e,fg,xi)
        elif(method=='multiple_root'):
            fn_p = request.form['fn_p']
            fn_p_p = request.form['fn_p_p']
            r = multiple_root.method(fx,fn_p,fn_p_p,xi,tol,iter,e)
        elif(method=='newton'):
            fnx = request.form['fnx']
            r = newton.method(tol,xi,iter,fx,fnx,e)
        elif(method=='secant'):
            xf = request.form['xf']
            r = secant.method(tol,xi,xf,iter,fx,e)
        else:
            return "The method is not valid"
        if(not r):
            return "something is wrong, please check your parameters"
        return r

api.add_resource(RootMethods, "/api/rootmethods/")