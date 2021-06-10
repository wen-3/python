# 1. 密碼輸入判斷
answer = str(1234)
guess = input("請輸入密碼：")

if guess == answer:
    print("歡迎光臨！")

# 2. 進階密碼判斷
answer = str(1234)
guess = input("請輸入密碼：")

if guess == answer:
    print("歡迎光臨！")
else:
    print("密碼錯誤！")

# 3. 延伸練習
score = int(input("請輸入成績："))

if score >= 60:
    print("成績及格！")
else:
    print("成績不及格！")

# 4. 判斷成績等第
score = int(input("請輸入成績："))

if score >= 90:
    print("優等")
elif score <= 89 and score >= 80:
    print("甲等")
elif score <= 79 and score >= 70:
    print("乙等")
elif score <= 69 and score >= 60:
    print("丙等")
else:
    print("丁等")

# 5.巢狀判斷式 - 判斷式內含判斷式
# 5.1 百貨公司折扣戰
sale = int(input("請輸入購物金額："))

if sale < 10000:
    sale = sale
else:
    if sale >= 100000:
        sale *= 0.8
    elif sale >= 50000:
        sale *= 0.85
    elif sale >= 30000:
        sale *= 0.9
    else:
        sale *= 0.95

print("{:.1f} 元".format(sale))

# 5.2 找出最大的數 - a,b,c為三個不同的數
a = int(input("請輸入 a 的值："))
b = int(input("請輸入 b 的值："))
c = int(input("請輸入 c 的值："))
max = 0

if a > b:
    max = a
else:
    max = b

if max > c:
    max = max
else:
    max = c

print("最大值為 {}".format(max))

# 6. 實作練習
# 6.1 實作題1 - 判斷奇偶數
num = int(input("請輸入正整數："))
if num % 2 == 1 :
    print("{} 為奇數！".format(num))
else:
    print("{} 為偶數！".format(num))

# 6.2 實作題2 - 所得稅課稅
money = int(input("請輸入今年收入淨額:"))
r = 0

if money <= 299999:
    r = 0
else:
    if money >= 2000000:
        r = 0.3
    elif money < 2000000 and money >= 1000000:
        r = 0.21
    elif money < 1000000 and money >= 600000:
        r = 0.13
    else:
        r = 0.6

money *= r
print("付稅金額：{:.1f} 元".format(money))

# 6.3 實作題3 - 華攝氏溫度轉換方式
n = int(input("溫度轉換選擇\n 1:華氏溫度轉換攝氏溫度\n 2:攝氏溫度轉換華氏溫度\n = "))
if n == 1:
    F = int(input("請輸入華氏溫度："))
    C = (5/9) * (F - 32)
    print("華氏 {} 等於攝氏 {:.1f}".format(F, C))
elif n == 2:
    C = int(input("請輸入攝氏溫度："))
    F = C * (9/5) + 32
    print("攝氏 {} 等於華氏 {:.1f}".format(C, F))
else:
    print("輸入錯誤")

# 6.4 實作題4 - 計算週薪資
money = 150
hour = int(input("請輸入本週工作時數："))
r = 1

if hour > 50:
    r = 1.6
else:
    if hour > 40 and hour <= 50:
        r = 1.2
    elif hour < 40:
        r = 0.8

pay = int((money * r) * hour)
print("本週薪資：", pay)
