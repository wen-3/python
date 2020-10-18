# 實作練習_5
# 寫法一
# num = int(input("請輸入3位數字:"))  # 777, 879
# num //= 10
# print(num * 10)

# 寫法二
# while True:
#     num = int(input("請輸入3位數字:"))
#     if num == 0:
#         print("結束")
#         break
#     num //= 10
#     print(num*10)

# 寫法三
import math
num = int(input("請輸入3位數字:"))  # 777, 879
num = math.floor(num / 10) * 10
print("執行結果:{}".format(num))
