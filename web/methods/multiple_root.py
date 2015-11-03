from astropy.table import Table
import parser, decimal, plot
c = raw_input("Absolute(a) or Relative(r) error?\n>")
abs_error = False
if c is 'a':
    abs_error = True

fn = raw_input("\nType the function:\n>f(x) = ")
fn_p = raw_input("\nType the differential of the function:\n>f'(x) = ")
fn_p_p = raw_input("\nType the second differential of the function:\n>f''(x) = ")
x0 = float(raw_input("\nType the initial value\n>"))
tol = float(raw_input("\nType the tolerance\n>"))
iterations = int(raw_input("\nType the maximum iterations\n>"))
y = parser.eval(fn, x0)
error = tol + 1
cont = 0
rows = []
s = "|\titers\t|\t\tXn\t|\t\tf(Xn)\t\t|\t\tError\t\t|\n"
while y != 0 and error > tol and cont < iter:
    y = parser.eval(fn, x0)
    y_prime = parser.eval(fn_p, x0)
    y_p_p = parser.eval(fn_p_p, x0)
    xn = x0 - (y*y_prime)/((y_prime*y_prime) - y*y_p_p)
    if abs_error:
        error = abs(xn-x0)
    else:
        error = abs((xn-x0)/xn)
    x0 = xn
    #s = s + "|\t"+str(cont)+"\t|\t"+str(xn)+"\t|\t"+str(y)+"\t\t|\t"+str(error)+"\t|\n"
    v = (cont,xn,y,error)
    rows.append(v)
    cont = cont+1
t = Table(rows=rows, names=('Iteraciones', 'xn', 'F(xn)', 'Error'))
print(t)
print("")
if y is 0:
    print x0,"is a root"
elif error <= tol:
    print x0,"is a root with error=",error
else:
    print "couldn't find any root after",cont,"iterations"

#print s
plot.graficar(fn)
