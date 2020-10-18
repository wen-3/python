# print
# print("多吃水果",60,100,sep=" & ",end=".")

# 字串格式化
name = "林小明"
score = 80
# print("%s的成績為:%d"%(name,score))

# price = 23.8275
# print("price is %8.2f"%price)

print("{}的成績為{}".format(name,score))
print("{0:5s}的成績為{1:3d}".format(name,score))  # 向左對齊,寬度為5,d寬度為3
# print("{0:<5s}的成績為{1:3d}".format(name,score))  # 向左對齊
print("{0:>5s}的成績為{1:3d}".format(name,score))  # 向右對齊
print("{0:^5s}的成績為{1:3d}".format(name,score)) # 置中