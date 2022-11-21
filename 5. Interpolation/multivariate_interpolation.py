from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

#                                           Multivariate Interpolation
# Polynomial and spline interpolations can be straightforwardly generalized to multivariate situations. In analogy with
# the univariate case, we seek a function whose values are given at a set of specified points and that can be evaluated
# for intermediary points within the sampled range. SciPy provides several functions and classes for multivariate
# interpolation, and in the following two examples, we explore two of the most useful functions for bivariate
# interpolation: the interpolate.interp2d and interpolate.griddata functions, respectively

# interpolate.interp2d, which is a straightforward generalization of the interp1d function that we previously used.
# This function takes the x and y coordinates of the available data points as separate one-dimensional arrays, followed
# by a two-dimensional array of values for each combination of x and y coordinates.

x = y = np.linspace(-2, 2, 10)


def f(x, y):
    return np.exp(-(x + .5) ** 2 - 2 * (y + .5) ** 2) - np.exp(-(x - .5) ** 2 - 2 * (y - .5) ** 2)


X, Y = np.meshgrid(x, y)
# Adding  noisy data at fixed grid points X, Y
Z = f(X, Y) + 0.05 * np.random.randn(*X.shape)

# ----------------------------------------------------------------------------------------------------------------------
f_i = interpolate.interp2d(x, y, Z, kind='cubic')  # Note that here x and y are one-dimensional arrays (of length 10),
# and Z is a two-dimensional array of shape (10, 10). The interp2d function returns a class instance, here f_i, that
# behaves as a function that we can evaluate at arbitrary x and y coordinates (within the sampled range).
# ----------------------------------------------------------------------------------------------------------------------

# Graphical representation

xx = yy = np.linspace(min(x), max(x), 100)
ZZi = f_i(xx, yy)  # despite being a 2D, the f_i function only takes 1D
XX, YY = np.meshgrid(xx, yy)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# for reference, first plot the contours of the exact function
c = axes[0].contourf(XX, YY, f(XX, YY), 15, cmap=plt.cm.RdBu)
axes[0].set_xlabel(r"$x$", fontsize=10)
axes[0].set_ylabel(r"$y$", fontsize=10)
axes[0].set_title("exact / high sampling")
cb = fig.colorbar(c, ax=axes[0])
cb.set_label(r"$z$", fontsize=10)
# next, plot the contours of the supersampled interpolation of the noisy data
c = axes[1].contourf(XX, YY, ZZi, 15, cmap=plt.cm.RdBu)
axes[1].set_ylim(-2.1, 2.1)
axes[1].set_xlim(-2.1, 2.1)
axes[1].set_xlabel(r"$x$", fontsize=10)
axes[1].set_ylabel(r"$y$", fontsize=10)
axes[1].scatter(X, Y, marker='x', color='k')
axes[1].set_title("interpolation of noisy data / low sampling")
cb = fig.colorbar(c, ax=axes[1])
cb.set_label(r"$z$", fontsize=10)

plt.show()

# For higher-dimensional problems, there is a function interpolate.interpnd, which is a generalization
# to N-dimensional problems.

# In SciPy we can use the interpolate.griddata for exactly this task. This function takes as first argument. a tuple of
# one-dimensional coordinate vectors (xdata, ydata) for the data values zdata, which are passed to the function in
# matrix form as third argument. The fourth argument is a tuple (X, Y) of coordinate vectors or coordinate matrices for
# the new points at which the interpolant is to be evaluated. Optionally, we can also set the interpolation method using
# the method keyword argument ('nearest', 'linear', or 'cubic'):

# Zi = interpolate.griddata((x, y), f(x, y), (X, Y), method='cubic')
