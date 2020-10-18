# 延伸練習_2
salary = int(input("請輸入薪資金額:"))  # 45000
prize= int(input("請輸入工作獎金:"))   # 8000
extra= int(input("請輸入加班費:"))   # 6250
total = salary + prize + extra
# print(f"本月實領獎金為{total:6f}")  (有點小問題)
print("本月實領獎金為" + str(total))

