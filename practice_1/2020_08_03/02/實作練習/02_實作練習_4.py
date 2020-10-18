# 實作練習_4
# 座標軸2個點之間的距離
import math
x1, y1 = 1, 8
x2, y2 = 3, 10
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("兩點距離為" + str(distance))

