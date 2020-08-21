import numpy as np
import numpy.random as random

goods=np.array([('Apple', 'supermarket', 25, 10),
('Macbook pro', '3C賣場', 45000, 1),
('iPhone 11', 'store', 23000, 1),
('泡麵', '便利商店', 45, 12 )])

print(goods[2])
print(goods[1:3])
print(goods[:2])
print(goods[-2])
print(goods[::-1])

a=np.arange(1,20, 2)
print(a)
print(a[a>=11])
print(a[~(a>=11)])
print(a[(a>=7)&(a<=15)])