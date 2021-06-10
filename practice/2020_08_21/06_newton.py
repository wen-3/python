# 使用牛頓法，求得能讓此函數為0的解
# 匯入牛頓法
from scipy.optimize import newton
def my_function(x):
    return (x**3 + 2*x + 1)
# 執行計算
print(newton(my_function,0))
# my_function()  可將執行結果代入驗證，可看是否近似0
