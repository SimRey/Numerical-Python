import numpy

line = 5
col = 3

f = lambda n, m: (n + 1) + 10 * m
arr = numpy.fromfunction(f, (line, col))

print(arr)
print(arr.shape)
print(arr.ndim)
print(arr[:, 1])

arr2 = numpy.arange(15, 56)
print(arr2)
arr2_inv = numpy.flip(arr2)  # arr2[::-1]
print(arr2_inv)
arr2[4] = 23
first_5 = arr2[:5]

diag_matrix = numpy.diag(first_5)
print(diag_matrix)
print(diag_matrix.ndim)

random_matrix = numpy.random.random((5, 3))
print(random_matrix)

product = diag_matrix @ random_matrix
print(product)

