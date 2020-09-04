import numpy as np
sample_multi_array_data2 = np.arange(16).reshape(4,4)
sample_multi_array_data2 

print('平方根:\n',np.sqrt(sample_multi_array_data2))

print('總和:',sample_multi_array_data2.sum())
print('最大値:',sample_multi_array_data2.max())
print('最小値:',sample_multi_array_data2.min())
print('平均:',sample_multi_array_data2.mean())
print('對角元素之和:',np.trace(sample_multi_array_data2))

