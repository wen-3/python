# 1. 串列
# 1.1 索引值
names = ["林小虎", "王中森", "邵木森"]
print(names[-1], names[-2])

# 1.2 串列切片練習
# 1.2.1 練習1
james = [23, 19, 22, 31, 18]
print(james[:3])
print(james[1:4])
print(james[::2])

# 1.2.2 練習2
warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print(warriors[:3])
print(warriors[1:])
print(warriors[-3:])

# 1.3 串列統計資料
james = [23, 19, 22, 31, 18]
print(max(james))
print(min(james))
print(sum(james))

# 1.4 改變串列元素
cars = ["Toyota", "Nissan", "Honda"]
cars[1] = "Ford"
print(cars)

# 1.5 串列結合
old_cars = ["Toyota", "Nissan", "Honda"]
cars = ["Audi", "BMW"]
news_cars = old_cars + cars
print(news_cars)

# 1.6 串列元素重複次數
cars = ["Audi", "BMW"]
print(cars*3)

# 2. 利用迴圈讀取串列
# 2.1 練習1 - 類似for each
list_1 = [12, "Apple", True]
for item in list_1:
    print(item)

# 2.2 練習2
names = ["林小虎", "王中森", "邵木森"]
for i in range(len(names)):
    print(f"編號：{i+1} 姓名：{names[i]}")

# 2.3 練習3
subjects=[" 國文"," 數學"," 英文"]
scores = [85, 79, 93]

length = len(subjects)
for i in range(length):
    print(f"{subjects[i]}成績：{scores[i]} 分")

# 2.4 練習4
names = ["林小虎", "王中森", "邵木森"]

for item in names[::-1]:
    print(item)
# 另一寫法
for item in reversed(names):
    print(item)

# 3. 串列搜尋與計次
# 3.1 搜尋
fruits = ["香蕉","蘋果","橘子"]
n = fruits.index("蘋果")
# m = fruits.index("梨子")  # 找不到會出現錯誤
print(n)
# print(m)

# 3.2 計算次數
fruits = ["香蕉","蘋果","橘子", "蘋果"]
n = fruits.count("蘋果")
m = fruits.count("梨子")
print(n)   # 傳回 2
print(m)   # 找不到會傳回 0

# 3.3 使用 in和not in運算式 結合 count()方法 & index()方法
# 如果串列內目前沒有這個水果，就將輸入的水果加入串列內
fruits = ["香蕉","蘋果","橘子"]
fruit = input("請輸入一個水果：")

# 方法一
search =  fruits.count(fruit)
if search == 0:
    fruits.append(fruit)
    print(fruits)

# 方法二
bool_value = fruit in fruits
if bool_value == False:
    fruits.append(fruit)
    print(fruits)

# 4. 串列新增和刪除
# 4.1 新增 - 成績
scores = []
time = 0
while(True):
    score = int(input("請輸入學生成績："))
    if score == -1:
        break
    scores.append(score)
    time += 1

print(f"共有 {time} 位學生")
print(f"本班總成績：{sum(scores)} 分，平均成績：{sum(scores)/time} 分")

# 4.2 新增 - 每周存款
deposits = []
for i in range(1,8):
    deposit = int(input(f"請輸入第 {i} 天的存款："))
    deposits.append(deposit)
print(f"存款總額：{sum(deposits)} 元")

# 4.3 刪除 - 水果
fruits = ["香蕉","蘋果","橘子","鳳梨","西瓜"]

while True:
    fruit = input("請輸入要刪除的水果(Enter 結束)：")
    if fruit in fruits:
        fruits.remove(fruit)
    else:
        if fruit == "":
            print("結束！")
            break
        print(f"{fruit} 不在串列中！")
    print(f"串列元素有：{fruits}")    

# 4.4 刪除 - 顏色
colors = ["紅","橙","黃","綠","藍"]

while True:
    color = input("請輸入要刪除的顏色(Enter 結束)：")
    if color in colors:
        colors.remove(color)
    else:
        if color == "":
            print("結束！")
            break
        print(f"{color} 不在串列中！")
    print(f"顏色有：{colors}")

# 5. 排序 - 成績由大到小排序
scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if inscore == "":
        print("輸入結束！")
        break
    scores.append(int(inscore))

scores2 = sorted(scores, reverse=True)
print(f"成績由大到小排序：{scores2}")

# 6. 實作練習
# 6.1 實作題1 - 收集串列中的奇數元素
numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]

odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print(f"result：{odd_numbers}")

# 6.2 實作題2 - 收集串列中的奇數元素，相同數字不可重複
numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]

odd_numbers = []
for number in numbers:
    if number % 2 == 1 and number not in odd_numbers:
        odd_numbers.append(number)
print(f"result：{odd_numbers}")

# 6.3 實作題3 - 找尋串列中是否包含此水果，並顯示該水果是串列中的第幾項 
fruits = ["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束)：")
    if fruit in fruits:
        print(f"{fruit} 在串列中的第 {fruits.index(fruit)+1} 項")
    else:
        if fruit == "":
            print("結束！")
            break
        print(f"{fruit} 不在串列中")

# 6.4 實作題4 - 找出成績最高分的同學，並顯示其姓名與成績
names = []
scores = []
for i in range(3):
    inname = input(f"請輸入第 {i+1} 同學的姓名：")
    inscore = input(f"請輸入第 {i+1} 同學的成績：")
    names.append(inname)
    scores.append(inscore)

highest = max(scores)
findIndex = scores.index(highest)
print(f"成績最高分的同學：\n姓名： {names[findIndex]}  成績： {highest}")

# 6.5 實作5 - 增加一平均欄位，平均分數取到小數點第1位
sc = [['洪錦魁', 80, 95, 88, 0],
      ['洪冰儒', 98, 97, 96, 0],
      ['洪雨星', 90, 91, 92, 0],
      ['洪冰雨', 91, 93, 95, 0],
      ['洪星宇', 92, 97, 90, 0],
]

length = len(sc)
for i in range(length):
    ch = sc[i][1]
    eng = sc[i][2]
    math = sc[i][3]
    inscore = [ch, eng, math]
    
    total = sum(inscore)
    sc[i][4] = total
    
    avg = total / 3
    sc[i].insert(5, round(avg, 1))
print(sc)

# 6.6 實作題6 - 儲存相同但沒有重複的元素
tp = (1,2,3,4,5,2,3,1,4)
tp = list(tp)
newtp = []
length = len(tp)

for i in range(length):
    if tp[i] not in newtp:
        newtp.append(tp[i])
newtp = tuple(newtp)
print(f"新的元組內容： {newtp}")
