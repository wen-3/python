import numpy as np
import numpy.random as random

num = np.arange(1,51)
print(num)
print('陣列總和:',num.sum())


a = random.randn(10)
print(a)
print("最大值：",a.max())
print("最小值：",a.min())
print("總和：",a.sum())


m = np.ones((5,5), dtype = np.float64)
mm = m*3
print(mm) # type is array
print(mm * mm)   # 陣列元素各自相乘
mm_new = np.mat(mm)  # 強制陣列轉換為矩陣
print(mm_new * mm_new)

# ma= np.ones((5,5), dtype="i") * 3
# print(m.dot(ma))

matrix= np.ones((5,5), dtype="i") * 3
print(matrix)
print(m.dot(matrix))

