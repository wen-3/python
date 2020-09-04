import numpy as np
sample_array1 = np.arange(12).reshape(3,4)
sample_array2 = np.arange(12).reshape(3,4)
print(np.concatenate([sample_array1,sample_array2],axis=0),'\n')
print(np.concatenate([sample_array1,sample_array2],axis=1))
