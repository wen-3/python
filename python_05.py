list1 = [1,'ABC',True]
list1[1]

name = ["林小虎","王中森","邵木淼"]
name[1:]

james = [23, 19, 22, 31, 18] 
print("james第1-3場得分",james[:3])
print("james第2-4場得分",james[1:4])
print("james第1,3,5場得分",james[::2])

names = ["林小虎","王中森","邵木淼"]
# for i in names:
#     print("編號：%s 姓名：%s" %((i+1) , names[i]))

subjects=[" 國文"," 數學"," 英文"]
scores = [85, 79, 93]
for i in range(len(scores)):
    print("%s成績：%d分" %(subjects[i],scores[i]))

names = ["林小虎","王中森","邵木淼"]
for i in range(len(names)-1,-1,-1):
    print(names[i])

# index() 搜尋
list1 = ["香蕉","蘋果","橘子"]
n = list1.index("蘋果")
# m = list1.index("梨子")
print(n)
# print(m)

# count() 計算次數
list1 = ["香蕉","蘋果","橘子"]
n = list1.count("蘋果")
m = list1.count("梨子")
print(n)
print(m)

james = ['Lebron James', 23, 19, 22, 31, 18] # 定義James串列
games = len(james)
score_Max = max(james[1:games])
i = james.index(score_Max)
print(james[0],"在第 %d 場得最高分 %d" %(i, score_Max))

scores = []
inscore = 0
while inscore != -1:
    inscore = int(input("請輸入學生的成績： "))  # [80, 100, 90]
    if inscore != -1:
        scores.append(inscore)
print("共有 %d 位學生" %(len(scores)))
total = sum(scores)
average = total / (len(scores))
print("本班總成績：%d 分，平均成績：%.2f 分" %(total, average))

moneys = []
i = 1
while i <= 7 :
    money = int(input("請輸入第" + str(i) + "天的存款"))  # [10,20,20,20,50,10,30]
    moneys.append(money)
    i += 1
total = sum(moneys)
print("存款總額：%d 元" %(total))

# 刪除串列中的水果
fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]
while True:
    print("串聯元素有：",fruits)
    fruit = input("請輸入要刪除的水果(直接輸入Enter結束)：")
    if fruit == "":
        break
    n = fruits.count(fruit)
    if  n > 0:
        fruits.remove(fruit)
    else:
        print(fruit,"不在串列中!")

# 刪除串列中的顏色
colors = ["紅", "橙", "黃", "綠", "藍"]
while True:
    print("串聯元素有：",colors)
    color = input("請輸入要刪除的顏色(直接輸入Enter結束)：")
    if color == "":
        break
    n = colors.count(color)
    if  n > 0:
        colors.remove(color)
        print("顏色有：", colors)
    else:
        print(color,"不在串列中!")
