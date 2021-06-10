# 1. 輸出與輸入
print(100, 60)
print(100, 60, sep="&")
print("hello", 100, 60)
print(100, 60, sep="&", end=".")

# 2.1 字串格式化
name = "小明"
age = 18
print("%s 的年齡是 %d" %(name, age)) # # 「%」字串格式化, %s 代表字串, %d 代表整數, %f 代表浮點數
print("{} 的年齡是 {}".format(name, age)) # 「format」字串格式化
print(f"{name} 的年齡是 {age}") # 「f-strings」字串格式化

# 2.2 字串格式化練習
# 2.2.1格式化列印成績單
# 空間與對齊 ^置中對齊 >靠右對齊 <靠左對齊
print("{:5s}{:^5s}{:^5s}{:^5s}{:^5s}".format("名字", "座號", "國文", "數學", "英文"))
print("{:5s}{:>4d}{:>7d}{:>7d}{:>7d}".format("林大明" ,1 ,100 ,87 ,79))
print("{:5s}{:>4d}{:>7d}{:>7d}{:>7d}".format("陳阿中" ,2 ,74 ,83 ,100))
print("{:5s}{:>4d}{:>7d}{:>7d}{:>7d}".format("張小英" ,11 ,82 ,65 ,8))

print("姓名 座號 國文 數學 英文")
print("{:3} {:2} {:3} {:3} {:3}".format("林大明" ,1 ,100 ,87 ,79))
print("{:3} {:2} {:3} {:3} {:3}".format("陳阿中" ,2 ,74 ,83 ,100))
print("{:3} {:2} {:3} {:3} {:3}".format("張小英" ,11 ,82 ,65 ,8))

# 2.2.2格式化年度稅額
print("{:2s}  {:3s}  {:3s}  {:3s}".format("年度", "所得稅", "營業稅", "證交稅"))
print("{:4d}  {:0>5.2f}  {:0>5.2f}  {:0>5.2f}".format(2017, 98.34, 90.2, 104.79))
print("{:4d}  {:0>5.2f}  {:0>5.2f}  {:0>5.2f}".format(2016, 83, 110.5, 82.45))
print("{:4d}  {:0>5.2f}  {:0>5.2f}  {:0>5.2f}".format(2015, 98, 79.32, 102))

# 3. input 輸入命令
# 3.1 計算成績總分
chinese = int(input("請輸入國文成績："))
math = int(input("請輸入數學成績："))
english = int(input("請輸入英文成績："))
sum_score = chinese + math + english
print("你的成績總分為：", sum_score)

# 4. 運算式
# 4.1 計算梯形面積
top = int(input("請輸入梯形上底長度："))
bottom = int(input("請輸入梯形下底長度："))
height = int(input("請輸入梯形高度："))
area = ((top + bottom) * height) / 2
print("梯形的面積為", area)

# 4.2 計算複利本金
i = 0.02
n = 6
p = int(input("請輸入本金存款金額："))
total = p * pow(1+i, n)
print("6年後的存款為：", total)

# 綜合練習
# 實作一
name1 = input("請輸入第一位學生的姓名：")
score1 = int(input("請輸入第一位學生的成績："))
name2 = input("請輸入第二位學生的姓名：")
score2 = int(input("請輸入第二位學生的成績："))
total = score1 + score2

print("姓名  成績")
print("{} {}".format(name1, score1))
print("{} {}".format(name2, score2))
print("成績總分為：" + str(total))

# 實作二
basis = 70
add = 30
n = int(input("請輸入路程公里數(整數)："))
pay = basis + add * (n-1)
print("你的車程車資費為：" + str(pay))

# 實作三
apple = 100
student = 23
print("蘋果可以吃的天數\n",apple // student)
print("第幾天產生蘋果不足供應\n", (apple // student)+1 )  # // -> 取商
print("不足數量\n", student - (apple % student))  # % -> 取餘數

# 實作四
x1, x2 = 1, 3
y1, y2 = 8, 10
d = float(((x1-x2)**2 + (y1-y2)**2)**(1/2)) # ** -> 次方
print("2點的距離是\n", d)

# 實作五
num = int(input("請輸入3位數數字："))
result = (num // 10) * 10
print("執行結果為：", result)
