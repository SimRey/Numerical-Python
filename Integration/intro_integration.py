from scipy import integrate
import numpy as np

#                                           Univariate integration
# The numerical quadrature routines in the SciPy integrate module can be categorized into two types: routines that take
# the integrand as a Python function and routines that take arrays with samples of the integrand at given points. The
# functions of the first type use Gaussian quadrature (quad, quadrature, fixed_quad), while functions of the second type
# use Newton-Cotes methods (trapz, simps, and romb).

# Example --> Gaussian quadrature

fun = lambda x, a: np.exp(-x ** a)

val, err = integrate.quad(fun, -np.inf, np.inf, args=(2))  # args=() substitutes missing variables
print(val, err)

# Non-continuous function
f = lambda x: 1 / np.sqrt(abs(x))

# value, error = integrate.quad(f, -1, 1)
# print(value) --> (inf, inf)

value, error = integrate.quad(f, -1, 1, points=[0])  # points=[] states the points not to be evaluated
print(value)

print()

# Example --> Newton-Cotes

fun_sqrt = lambda x: np.sqrt(x)
a, b = 0, 2
x = np.linspace(a, b, 65)
y = fun_sqrt(x)

# Simpson and trapezoidal rule
val_trapz = integrate.trapz(y, x)
print(val_trapz)

val_simps = integrate.simps(y, x)
print(val_simps)

# The trapz and simps functions do not provide any error estimates

# The Romberg method is a Newton-Cotes method but one that uses Richardson extrapolation to accelerate the convergence
# of the trapezoid method; however this method does require that the sample points are evenly spaced and also that
# there are 2^n+1 sample points, where n is an integer. Like the trapz and simps methods, romb takes an array with
# integrand samples as first argument, but the second argument must (if given) be the sample-point spacing dx.

pow = 1 + 2 ** 6
x_romb = np.linspace(a, b, pow)
dx = x_romb[1] - x_romb[0]
y_romb = fun_sqrt(x_romb)
val_romb = integrate.romb(y_romb, dx=dx)
print(val_romb)

print()
print()


# ----------------------------------------------------------------------------------------------------------------------
#                                          Multiple integration
# Multiple integrals, such as double integrals and triple integrals can be evaluated using the dblquad and tplquad
# functions from the SciPy integrate module. Also, integration over n variables over some domain D, can be evaluated
# using the nquad function. These functions are wrappers around the single-variable quadrature function quad, which is
# called repeatedly along each dimension of the integral.

# Example for triple integral (double, lambda fun oly takes x dependant variables in the first integral)

def f(x, y, z):
    return np.exp(-x ** 2 - y ** 2 - z ** 2)


g, h = 0.1, 1
i, j = lambda x: 2 * x ** 2 + 15 * x + 3, lambda x: np.sqrt(x)
k, l = lambda x, y: x*y**2 - x + 1/y, lambda x, y: np.sqrt(1/(x*y))

res_triple = integrate.tplquad(f, g, h, i, j, k, l)
print(res_triple)
