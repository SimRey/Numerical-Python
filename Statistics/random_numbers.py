import numpy as np
import matplotlib.pyplot as plt

# The random library contains many functions to display random numbers, for example np.random.rand is a function which
# generates uniformly distributed floating-point numbers in the half-open interval [0, 1) (i.e., 0.0 is a possible
# outcome, but 1.0 is not). The randn function produces random numbers that are distributed according to the standard
# normal distribution (the normal distribution with mean 0 and standard deviation 1), and the randint function generates
# uniformly distributed integers between a given low (inclusive) and high (exclusive) value.

rand_num = np.random.randn(2, 5)
print(rand_num)

rand_int = np.random.randint(-10, 10, size=(2, 5))
print(rand_int)

fig, axes = plt.subplots(1, 3, figsize=(12, 3))
axes[0].hist(np.random.rand(10000), edgecolor="black")
axes[0].set_title("rand")
axes[1].hist(np.random.randn(10000), edgecolor="black")
axes[1].set_title("randn")
axes[2].hist(np.random.randint(low=1, high=10, size=10000), bins=9,
             align='left', edgecolor="black")  # bins= number of columns
axes[2].set_title("randint(low=1, high=10)")

plt.show()
