import numpy as np
sample_array3 = np.array([[1,2,3],[4,5,6]])
sample_array4 = np.array([[7,8,9],[10,11,12]])
sample_array_vstack = np.vstack((sample_array3,sample_array4))
# 顯示產生的資料sample_array_vstack
sample_array_vstack

# 將sample_array_vstack分割為3個，代入first、seocnd、third這3個變數
first,second,third=np.split(sample_array_vstack,[1,3])
# 顯示first
print(first)
print(second)
print(third)
