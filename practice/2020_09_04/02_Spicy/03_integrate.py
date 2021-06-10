# 積分計算
from scipy import integrate
import math
def calcPi(x):
    return 4/(1+x**2)
# 計算結果與估計誤差
integrate.quad(calcPi, 0, 1)

# 積分計算
from scipy import integrate
import math
def calcPi(x):
    return (x + 1)**2
# 計算結果與估計誤差
integrate.quad(calcPi, 0, 2)

