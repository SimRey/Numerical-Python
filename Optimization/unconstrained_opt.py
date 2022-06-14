#                                                 Optimization
# In this chapter we discuss using SciPy’s optimization module optimize for nonlinear optimization problems, and we
# will briefly explore using the convex optimization library cvxopt for linear optimization problems with linear
# constraints. This library also has powerful solvers for quadratic programming problems.

from scipy import optimize as opt
import matplotlib.pyplot as plt
import numpy as np


#                                      Univariate and unconstrained optimization

# In SciPy’s optimize module, the brent function is such a hybrid method, and it is generally the preferred method
# for optimization of univariate functions with SciPy. This method is a variant of the golden section search method
# that uses inverse parabolic interpolation to obtain faster convergence. Instead of calling the optimize.golden and
# optimize.brent functions directly, it is convenient to use the unified interface function optimize.minimize_scalar,
# which dispatches to the optimize.golden and optimize.brent functions depending on the value of the method keyword
# argument, where the currently allowed options are 'Golden', 'Brent', or 'Bounded'.

# Example: minimizing the area of a cylinder with a unit volume
# Definition of the objective function (univariate --> perform necessary changes if needed)
# f ([r, h]) = 2πr^2+2πrh           g([r, h]) = πr2h − 1 = 0
# h = 1/πr^2 --> f ([r]) = 2πr^2+2/r

f = lambda r: 2 * np.pi * r ** 2 + 2 / r
r_min = opt.minimize_scalar(f, bracket=(0.1, 4), method="Brent")

print(r_min)
print(f"The minimum radius is {r_min.x}, giving an area of {r_min.fun}")

print()
print()


#                                       Unconstrained Multivariate Optimization


def funn(var):
    x1 = var[0]
    x2 = var[1]
    return (x1 - 1) ** 4 + 5 * (x2 - 1) ** 2 - 2 * x1 * x2


x_opt = opt.minimize(funn, [0, 0], method='SLSQP')
print(x_opt.x)
