from scipy.optimize import fsolve
def f(x):
    y = 5 * x - 10
    return y

x = fsolve(f,0)
print(x)
