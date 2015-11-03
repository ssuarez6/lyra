from flask_restful import Resource, request
from app import api
from methods import bisection

class Methods(Resource):
    def get(self):
        xi = request.args.get('xi')
        fx = request.args.get('fx')
        xf = request.args.get('xf')
        tol= request.args.get('tol')
        iter = request.args.get('iter')
        e = request.args.get('e')
        print fx
        print xi
        print "____________________________________________"
        return bisection.bisection(fx,xi,xf,tol,iter,1)

api.add_resource(Methods, "/api/")