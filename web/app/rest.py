from flask_restful import Resource, request
from app import api
from methods import bisection, regula_falsi, fixed_point, \
    multiple_root, newton, secant


class Methods(Resource):

    def post(self):
        fx = request.form['fx']
        tol= request.form['tol']
        iter = request.form['iter']
        xi = request.form['xi']
        e = request.form['e']
        method = request.form['method']
        r = None
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

api.add_resource(Methods, "/api/")