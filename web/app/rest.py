from flask_restful import Resource, request
from app import api
from methods import bisection, regula_falsi


class Methods(Resource):

    def post(self):

        fx = request.form['fx']
        tol= request.form['tol']
        iter = request.form['iter']
        e = request.form['e']
        method = request.form['method']
        r = None
        if(method == 'bisection'):
            xi = request.form['xi']
            xf = request.form['xf']
            r = bisection.method(fx,xi,xf,tol,iter,e)
        elif(method=='regula_falsi'):
            xi = request.form['xi']
            xf = request.form['xf']
            r = regula_falsi.method(fx,xi,xf,tol,iter,e)
        if(not r):
            return "The method is not valid"
        return r

api.add_resource(Methods, "/api/")