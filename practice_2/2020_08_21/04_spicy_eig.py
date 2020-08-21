import numpy as np
import scipy.linalg as linalg

matrix = np.array([[2,-12], [1,-5]])
eig_value, eig_vector = linalg.eig(matrix)
print(eig_value)
print(eig_vector)
