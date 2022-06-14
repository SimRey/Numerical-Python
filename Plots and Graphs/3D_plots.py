import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(8, 6), subplot_kw={'projection': '3d'})
x = np.linspace(-5, 5, 101)
y = np.cos(x)
z = np.exp(y) + 2 * np.sin(x)
ax.plot(x, y, z)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_title("Contour")

plt.show()

# This feature enables to plot like in 2D

# Surface plot
axis = plt.axes(projection="3d")

z1 = lambda a, b: np.sin(np.sqrt(a ** 2 + b ** 2))

x1 = np.linspace(-5, 5, 101)
y1 = x1

X, Y = np.meshgrid(x1, y1)  # Transforming vectors to matrices to plot the surface
Z = z1(X, Y)

axis.plot_surface(X, Y, Z)
axis.set_xlabel("$x$")
axis.set_ylabel("$y$")
axis.set_zlabel("$z$")
axis.set_title("Surface")

plt.show()
