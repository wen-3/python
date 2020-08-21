import numpy as np
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

# 散佈圖
import numpy.random as random # 固定種子值
random.seed(0)

# x軸
x = np.random.randn(30)

# y軸
y = np.sin(x) + np.random.randn(30)

# 指定圖形的大小
plt.figure(figsize=(20, 6))

# 描繪圖形
plt.plot(x, y, 'o') #也能如下描繪散佈圖
#plt.scatter(x, y)

# 標題
plt.title('Title Name')

# X的座標名稱
plt.xlabel('X')

# Y的座標名稱
plt.ylabel('Y')

# 顯示grid（圖形中的格線）
plt.grid(True)

