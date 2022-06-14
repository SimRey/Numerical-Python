from scipy import optimize as opt
import matplotlib.pyplot as plt
import numpy as np


# Constraints add another level of complexity to optimization problems, and they require a classification of their own.
# A simple form of constrained optimization is the optimization where the coordinate variables are subject to some
# bounds. For example: minx f (x ) subject to 0 ≤ x ≤ 1. The constraint 0 ≤ x ≤ 1 is simple because it only restricts
# the range of the coordinate without dependencies on the other variables. This type of problems can be solved using
# the L-BFGS-B method in SciPy.

# Example
# f (x) = (x1 − 1)^2 − (x2 − 1)^2 subject to the constraints 2 ≤ x1 ≤ 3 and 0 ≤ x2 ≤ 2.

def fun(var):
    x1 = var[0]
    x2 = var[1]
    return (x1 - 1) ** 2 - (x2 - 1) ** 2


bnd_x1, bnd_x2 = (2, 3), (0, 2)
x0 = np.array([1, 1])

# Without constrain
x_opt = opt.minimize(fun, x0, method='L-BFGS-B')
print(x_opt.x)

# With constrain
x_cons_opt = opt.minimize(fun, x0, method='L-BFGS-B', bounds=[bnd_x1, bnd_x2])
print(x_cons_opt.x)

print()


# The method known as sequential least square programming, abbreviated as SLSQP, which is available in the SciPy as the
# optimize.slsqp function and via optimize.minimize with method='SLSQP'. The optimize.minimize function takes the
# keyword argument constraints, which should be a list of dictionaries that each specifies a constraint. The allowed
# keys (values) in this dictionary are type ('eq' or 'ineq'), fun (constraint function), jac (Jacobian of the constraint
# function), and args (additional argument to constraint function and the function for evaluating its Jacobian).

# Enriching the previous example with a constrain function g(x) = x2 − 1.75 − (x1 − 0.75)^4 ≥ 0

def g(var):
    x1 = var[0]
    x2 = var[1]
    return x2 - 1.75 - (x1 - 0.75) ** 4


cons = [dict(type='ineq', fun=g)]
x_cons_opt_2 = opt.minimize(fun, x0, method='SLSQP', constraints=cons, bounds=[bnd_x1, bnd_x2])
print(x_cons_opt_2.x)

# For optimization problems with only inequality constraints, SciPy provides an alternative solver using the constrained
# optimization by linear approximation (COBYLA) method. This solver is accessible either through optimize.fmin_cobyla
# or optimize. minimize with method='COBYLA'. This method doesn't handle bounds.

x_cons_opt_3 = opt.minimize(fun, x0, method='COBYLA', constraints=cons)
print(x_cons_opt_3.x)
