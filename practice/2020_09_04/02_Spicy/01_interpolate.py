# 線性內插
from scipy import interpolate
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.sin(x**2/5.0)
plt.plot(x,y,'o')
plt.grid(True)

# from scipy import interpolate
# ?interpolate.interp1d
