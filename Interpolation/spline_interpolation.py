from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

#                                                   Spline
# A spline is a special type of piecewise polynomial interpolant: a piecewise polynomial of degree k is a spline if it
# is continuously differentiable k − 1 times. The most popular choice is the third-order spline, k = 3, which requires
# 4(n − 1) parameters. The SciPy interpolate module provides several functions and classes for performing spline
# interpolation. For example, we can use the interpolate.interp1d function, which takes x and y arrays for the data
# points as first and second arguments. The optional keyword argument kind can be used to specify the type and order of
# the interpolation. In particular, we can set kind=3 (or, equivalently, kind='cubic') to compute the cubic spline.

runge = lambda x: 1 / (1 + 25 * x ** 2)

x = np.linspace(-1, 1, 11)
y = runge(x)
f_i = interpolate.interp1d(x, y, kind=3)

xx = np.linspace(-1, 1, 100)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(xx, runge(xx), 'k', lw=1, label="Runge's function")
ax.plot(x, y, 'ro', label='sample points')
ax.plot(xx, f_i(xx), 'r--', lw=2, label='spline order 3')
ax.legend()
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_ylabel(r"$y$", fontsize=10)
ax.set_xlabel(r"$x$", fontsize=10)
ax.set_title(r"Spline interpolation $\frac{1}{1 + 25 x^2}$", fontsize=15)

plt.show()
