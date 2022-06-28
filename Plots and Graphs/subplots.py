import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#                                                       Subplots
# It is often the case when plotting grids of subplots that either the x or the y axis, or both, is shared among
# the subplots. Using the sharex and sharey arguments to plt.subplots can be useful in such situations, since it
# prevents the same axis labels to be repeated across multiple Axes.
# It is also worth noting that the dimension of the NumPy array with Axes instances that is returned by plt.subplots
# is “squeezed” by default: that is, the dimensions with length 1 are removed from the array. If both the requested
# numbers of column and row are greater than one, then a two-dimensional array is returned, but if either (or both) the
# number of columns or rows is one, then a one-dimensional (or scalar, i.e., the only Axes object itself ) is returned.
# We can turn off the squeezing of the dimensions of the NumPy arrays by passing the argument squeeze=False to the
# plt.subplots function.

fig, axes = plt.subplots(2, 2, figsize=(6, 6), sharex=True, sharey=True, squeeze=False)

x1 = np.random.randn(100)
x2 = np.random.randn(100)

axes[0, 0].set_title("Uncorrelated")
axes[0, 0].scatter(x1, x2)

axes[0, 1].set_title("Weakly positively correlated")
axes[0, 1].scatter(x1, x1 + x2)

axes[1, 0].set_title("Weakly negatively correlated")
axes[1, 0].scatter(x1, -x1 + x2)

axes[1, 1].set_title("Strongly correlated")
axes[1, 1].scatter(x1, x1 + 0.15 * x2)

axes[1, 1].set_xlabel("x")
axes[1, 0].set_xlabel("x")
axes[0, 0].set_ylabel("y")
axes[1, 0].set_ylabel("y")

plt.show()

#                                                   GridSpec
# This is the most general grid layout manager in Matplotlib, and in particular it allows creating grids where not
# all rows and columns have equal width and height.

# Example
x = np.linspace(-5, 5, 101)
figu = plt.figure(figsize=(6, 4))
gs = mpl.gridspec.GridSpec(4, 4)

ax0 = figu.add_subplot(gs[0, 0])
ax01 = figu.add_axes(ax0)
ax01.plot(x, x)

ax1 = figu.add_subplot(gs[1, 1])
ax11 = figu.add_axes(ax1)
ax11.plot(x, np.sin(x))

ax2 = figu.add_subplot(gs[2, 2])
ax21 = figu.add_axes(ax2)
ax21.plot(x, np.cos(x))

ax3 = figu.add_subplot(gs[3, 3])
ax31 = figu.add_axes(ax3)
ax31.plot(x, x**2)

ax4 = figu.add_subplot(gs[0, 1:])
ax41 = figu.add_axes(ax4)
ax41.plot(x, x**3)

ax5 = figu.add_subplot(gs[1:, 0])
ax51 = figu.add_axes(ax5)
ax51.plot(x, np.tan(x))

ax6 = figu.add_subplot(gs[1, 2:])
ax61 = figu.add_axes(ax6)
ax61.plot(x, np.exp(x))

ax7 = figu.add_subplot(gs[2:, 1])
ax71 = figu.add_axes(ax7)
ax71.plot(x, np.sqrt(x))

ax8 = figu.add_subplot(gs[2, 3])
ax81 = figu.add_axes(ax8)
ax81.plot(x, np.log(x))

ax9 = figu.add_subplot(gs[3, 2])
ax91 = figu.add_axes(ax9)
ax91.plot(x, np.arcsin(x))

plt.show()
