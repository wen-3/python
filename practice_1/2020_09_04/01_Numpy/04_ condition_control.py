# numpy.where（條件的陣列, X資料, Y資料）
import numpy as np
x_array= np.array([1,2,3,4,5])
y_array= np.array([6,7,8,9,10])
cond_data = np.array([False,False,True,True,False])
print(np.where(cond_data, x_array, y_array))
