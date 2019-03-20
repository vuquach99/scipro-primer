from math import pi, exp, sqrt
def gaussian(m, s, x):
    f = (1/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)
    return f

print (gaussian(0, 2, 1))