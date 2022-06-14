# Non-linear equations
import numpy as np
import sympy as sym

# Symbolic resolution
x, a, b = sym.symbols("x, a, b")
sol = sym.solve(a * sym.cos(x) - b * sym.sin(x), x)
print(sol)

# In general nonlinear equations are typically not solvable analytically. For example, equations that contain both
# polynomial expressions and elementary functions, such as sinx = x, are often transcendental and do not have an
# algebraic solution. If we attempt to solve such an equation using SymPy, we obtain an error in the form of an
# exception:

# sym.solve(sympy.sin(x)-x, x) --> NotImplementedError: multiple generators [x, sin(x)]
# No algorithms are implemented to solve equation -x + sin(x)

# ----------------------------------------------------------------------------------------------------------------
# Optimize module
from scipy import optimize as opt

# The SciPy optimize module provides multiple functions for numerical root finding. The optimize.bisect and
# optimize.newton functions implement variants of bisection and Newton methods. The optimize.bisect takes three
# arguments: first a Python function (e.g., a lambda function) that represents the mathematical function for the
# equation for which a root is to be calculated and the second and third arguments are the lower and upper values
# of the interval for which to perform the bisection method. Note that the sign of the function has to be different
# at the points a and b for the bisection method to work, as discussed earlier.

# Taking as an example exp(x) -2
f_sol = opt.bisect(lambda x: np.exp(x) - 2, -2, 2)
print(f_sol)

# Newton method
x_root_guess = 0
f = lambda x: np.exp(x) - 2
fprime = lambda x: np.exp(x)  # the derivative is calculated
f_newton = opt.newton(f, x_root_guess)
print(f_newton)
f_advanced_newton = opt.newton(f, x_root_guess, fprime=fprime)  # more accurate
print(f_advanced_newton)
print()
print()


# The SciPy optimize module provides additional functions for root finding. In particular, the optimize.brentq and
# optimize.brenth functions, which are variants of the bisection method, also work on an interval where the
# function changes sign.

# ---------------------------------------------------------------------------------------------------------------------
# Systems of Nonlinear Equations
# Taking as an example the following system of nonlinear equations:
#       y - x^3-2x^2+1 = 0
#       y+x^2-1 = 0
# To solve this equation system using SciPy, we need to define a Python function for f ([x1, x2]) and call, for example,
# the optimize.fsolve using the function and an initial guess for the solution vector:


def f(var):
    x = var[0]
    y = var[1]
    return [y - x ** 3 - 2 * x ** 2 + 1, y + x ** 2 - 1]


guess = [1, 1]
sol, infodict, ier, mesg = opt.fsolve(f, guess, full_output=True)
print(sol)
Jacobian = (infodict["fjac"])
eigenvalues = np.linalg.eigvals(Jacobian)
print(eigenvalues) # Eigenvalues are calculated form the Jacobian matrix displayed from the fsolve function

# To specify a Jacobian for optimize.fsolve to use, we need to define a function that evaluates the Jacobian for a
# given input vector. This requires that we first derive the Jacobian by hand or, for example, using SymPy

x, y = sym.symbols("x, y")
f_mat = sym.Matrix([y - x ** 3 - 2 * x ** 2 + 1, y + x ** 2 - 1])
jacob = f_mat.jacobian(sym.Matrix([x, y]))
print(jacob)


def jacobian(v):
    x = v[0]
    return [[-3 * x ** 2 - 4 * x, 1], [2 * x, 1]]


accu_sol = opt.fsolve(f, guess, fprime=jacobian)  # As it can be seen it's not necessary, results are the same
print(accu_sol)
