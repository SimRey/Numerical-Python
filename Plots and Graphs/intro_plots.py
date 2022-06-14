import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#                                                       Plotting basics

# First example
x = np.linspace(-5, 2, 100)
y1 = x ** 3 + 5 * x ** 2 + 10
y2 = 3 * x ** 2 + 10 * x
y3 = 6 * x + 10

fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="$y(x): x^3 + 5x^2 + 10$")
ax.plot(x, y2, color="red", label="$y'(x): 3x^2 + 10x$")
ax.plot(x, y3, color="green", label="$y''(x): 6x + 10$")
ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(loc="best")

plt.show()

# Here we used the plt.subplots function to generate Figure and Axes instances. This function can be used to create
# grids of Axes instances within a newly created Figure instance, but here it was merely used as a convenient way of
# creating a Figure and an Axes instance in one function call. Once the Axes instance is available, note that all the
# remaining steps involve calling methods of this Axes instance.

fig.savefig("graph.png", dpi=100, facecolor="#f1f1f1")  # This command enables to save the created figure

#                                                       Figure
# A Figure object can be created using the function plt.figure, which takes several optional keyword arguments for
# setting figure properties. In particular, it accepts the figsize keyword argument, which should be assigned to a
# tuple on the form (width, height), specifying the width and height of the figure canvas in inches. It can also be
# useful to specify the color of the figure canvas by setting the facecolor keyword argument.

figu = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")

