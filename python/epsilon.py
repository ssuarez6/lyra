delta = 0.5
i = 1.0
print "Delta +1 diff 0\n"
while delta+i != i:
    print delta
    delta /= 2

delta = 0.5
print "Delta diff 0\n"
while delta!=0:
    print delta
    delta /= 2

print "Bye\n"
print "****************************\n"
print "Con Decimal"
from decimal import *
getcontext().prec = 300
delta = Decimal(0.5)
print "Delta diff 0\n"
while delta!=0:
    print delta
    delta /= 2

print delta
print "BYE!"
