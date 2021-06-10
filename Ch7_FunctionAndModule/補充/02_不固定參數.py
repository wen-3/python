# 不固定參數
def add(n1, *n2):
    t = 0
    for i in n2:
        t += i
    return t+n1

def calsum(bb, cc, *params):
    total = 0
    for param in params:
        total += param
    return total**bb-cc