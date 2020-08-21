import scipy.linalg as linalg
matrix = np.array([[1, 2, 3], [1, 3, 2], [3, 1, 2]])
det_value = linalg.det(matrix)
inv_value = linalg.inv(matrix)
eig_value, eig_vector = linalg.eig(matrix)
print("行列式", det_value)
print("反矩陣", inv_value)
print("特徵值", eig_value)
print("特徵向量", eig_vector)
