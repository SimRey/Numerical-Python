#                                       Least squares method
# The least squares method is a statistical procedure to find the best fit for a set of data points by minimizing the
# sum of the offsets or residuals of points from the plotted curve. Least squares regression is used to predict the
# behavior of dependent variables.

from scipy import linalg as la
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Defining the true model parameters
x = np.linspace(-1, 1, 100)
a, b, c = 1, 2, 3
y = a + b * x + c * x ** 2

# Data with noise
m = 100
X = 1 - 2 * np.random.rand(m)
Y = a + b * X + c * X ** 2 + np.random.randn(m)

# fit the data to the model using linear least square
A = np.vstack([X ** 0, X ** 1, X ** 2])
sol, r, rank, sv = la.lstsq(A.T, Y)

y_fit = sol[0] + sol[1] * x + sol[2] * x ** 2


r2 = r2_score(y, y_fit)
print(r2)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(X, Y, 'go', alpha=0.5, label='Simulated data')
ax.plot(x, y, 'k', lw=2, label=r'True value $y = 1 + 2x + 3x^2$')
ax.plot(x, y_fit, 'b', lw=2, label='Least square fit')
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$y$", fontsize=18)
ax.legend(loc=2)
plt.show()
