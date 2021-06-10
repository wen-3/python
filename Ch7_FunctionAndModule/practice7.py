# 1. 自訂函式
# 1.1 攝氏轉華氏
def tem(c):
    f = c*1.8 + 32
    f = round(f, 1)
    return f

c = int(input("請輸入攝氏溫度："))
print(f"華氏溫度為： {tem(c)} 度")

# 1.2 公斤轉英鎊
def weight(kg):
    pound = kg * 2.2
    pound = round(pound, 1)
    return pound

kg = int(input("請輸入體重公斤數："))
print(f"你的體重為：{weight(kg)} 鎊")

# 2. 數值凾式
# 2.1 學生均分蘋果
def fruit(stu, apple):
    stu = apple // stu
    apple = apple % stu
    print(f"每個學生可分得蘋果 {stu} 個\n蘋果剩餘 {apple} 個")

stu = int(input("請輸入學生人數："))
apple = int(input("請輸入蘋果總數："))
fruit(stu, apple)

# 2.2 生活費
def money(life, expenses):
    setMoney = divmod(life, expenses)
    listMoney = list(setMoney)
    print(f"可維持生活 {listMoney[0]} 天\n生活費剩餘 {listMoney[1]} 元")

life = int(input("請輸入總生活費："))      # 10,000
expenses = int(input("請輸入每天花費："))  # 350
money(life, expenses)

# 2.3 總和及排序
def elec(listExpenses):
    print(f"最多電費為：{max(listExpenses)}")
    print(f"最少電費為：{min(listExpenses)}")
    print(f"電費總和為：{sum(listExpenses)}")
    print(f"電費由大到小排序為：{sorted(listExpenses, reverse=True)}")

listExpenses = []
while True:
    expense = int(input("請輸入電費 (-1：結束)："))
    if expense != -1:
        listExpenses.append(expense)
    else:
        break
length = len(listExpenses)
print(f"共輸入 {length} 個數")
elec(listExpenses)

# 2.4 4個月的家庭支出狀況
def money(listExpenses):
    print(f"支出最多的金額為：{max(listExpenses)}")
    print(f"支出最少的金額為：{min(listExpenses)}")
    print(f"支出的總和為：{sum(listExpenses)}")
    print(f"支出金額由小到大排序為：{sorted(listExpenses)}")

listExpenses = []
for i in range(4):
    expense = int(input(f"請輸入第 {i+1} 個月的支出金額："))
    listExpenses.append(expense)
money(listExpenses)

# 3. 字串凾式
# 3.1 檢查圖片格式
def check(name):
    bool = name.endswith("jpg")
    if bool == True:
        print("圖片格式是 JPG！")
    else:
        print("圖片格式不是 JPG！")
name = input("請輸入圖片檔案名稱：")  # picture.jpg / picture.png
check(name)

# 3.2 以字串排版函式列印成績單 - ljust & rjust
name = ["林大明", "陳阿中", "張小英"]
number = [1, 2, 3]
chinese = [100, 74, 82]
math = [87, 88, 65]
eng = [79, 100, 8]

print("姓名".ljust(5) + "座號".rjust(3) + "國文".rjust(4) + "數學".rjust(4) + "英文".rjust(4))
for i in range(3):
    print(name[i].ljust(5) + str(number[i]).rjust(4) + str(chinese[i]).rjust(6) + str(math[i]).rjust(6) + str(eng[i]).rjust(6))

# 3.3 轉換日期格式 - replace()
date = "2017-8-23"
newDate = ( "-" + date + "-").replace("-", "西元", 1).replace("-", "年", 1).replace("-", "月", 1).replace("-", "日", 1)
print(f"轉換前的日期格式：{date}")
print(f"轉換後的日期格式：{newDate}")

# 3.4 轉換時間格式
time = "10:23:41"
newTime = ( time + ":").replace(":", "點", 1).replace(":", "分", 1).replace(":", "秒", 1)
print(f"轉換前的時間格式：{time}")
print(f"轉換後的時間格式：{newTime}")

# 4. 亂數模組
# 4.1 擲骰子遊戲 - randint
import random as r
while True:
    start = input("按任意鍵再按[ENTER]鍵擲骰子，直接按[ENTER] 鍵結束：")
    if start != "":
        num = r.randint(1, 6)
        print(f"你擲的骰子點數為：{num}")
    else:
        print("結束")
        break

# 4.2 大富翁遊戲
import random as r
sum = 0
for i in range(3):
    num = r.randint(1, 6)
    print(f"第 {i+1} 次投擲數為 {num}")
    sum += num
print(f"遊戲前進步數為 {sum}")

# 4.3 大樂透中獎號碼 - sample()
import random as r
numbers = list(range(1,50))
numList = r.sample(numbers, 7)
print(f"本期大樂透中獎號碼為：{numList}")
print()
specialNum = numList[-1]
sortNumList = sorted(numList[:-1])
sortNumString = [str(num) for num in sortNumList]
print(f"本期大樂透中獎號碼排序後為：{', '.join(sortNumString)}")
print(f"本期大樂透特別號為：{specialNum}")

# 4.4 四星彩中獎號碼
import random as r
numbers = list(range(0, 10))
lottery = r.sample(numbers, 4)
print(f"本期四星彩中獎號碼為：{lottery}")
sortLottery = sorted(lottery)
sortLotteryString = [str(num) for num in sortLottery]
print(f"本期四星彩中獎號碼排序後為：{', '.join(sortLotteryString)}")

# 5. 時間模組
# 5.1 列印時間函式所有資訊 - localtime
import time as t
result = t.localtime()
print(result)
print("\n類型：" , type(result))
transform = t.strftime("西元 %Y 年 %m 月 %d 日 %H 點 %M 分 %S 秒 %A", result)
print(transform)

# 5.2 判斷今天是上半年或下半年
import time as t
result = t.localtime()
# print(result)
month = result.tm_mon
if month <= 6:
    print("現在是上半年")
else:
    print("現在是下半年")

# 5.3 計算執行一百萬次整數運算的時間 - 寫法不確定
import time as t
start = t.process_time()
for i in range(1000000):
    i
end = t.process_time()
print(end - start)

# 6.專題
# 6.1 函數的應用 - 用函數重新設計記錄一篇文章每個單字出現次數
# 查詢網路方法並做修正
# 將所傳來的字串有標點符號部分用空白字元取代
def modifySong(word):
    word = word.replace(",", "").replace("?", "").replace(".", "")
    # print(word)
    word = word.lower()   # 將字串字元都轉為小寫字母
    return word

# 將字串轉成串列，同時將串列轉成字典，最後遍歷字典然後記錄每個單字出現的次數
def wordCount(word):
    wordList = word.split(" ")
    # print(wordList)
    wordSet = set(wordList)  # 為了去除重複的項，將 list轉為 set
    # print(wordSet)

    wordDict = {}
    for item in wordSet:
        n = wordList.count(item)  # 計算某個單字(item)在 wordList裡出現幾次
        wordDict.update({item:n})
    return wordDict

data = """Are you sleeping, are you sleeping, Brother John, Brother John? Morning bells are ringing, morning bells are ringing. Ding ding dong, Ding ding dong."""

data = modifySong(data)
result = wordCount(data)
print(result)

# 6.2 質數 Prime Number
# 6.2.1 使用 for else
def isPrime(num):
    for i in range(2, num):
        # result = num % i
        if num % i == 0:
            print(f"{num} 不是質數")
            break
    else:
        print(f"{num} 是質數")

num = int(input("請輸入數字："))
isPrime(num)

# 6.2.2 使用 def -> true & false
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("請輸入數字："))
if isPrime(num):
    print(f"{num} 是質數")
else:
    print(f"{num} 不是質數")

# 6.3 遞迴式函數設計 recursive - 執行階乘(factorial)運算
sum = 1
num = int(input("請輸入一個正整數進行運算："))
i = 1
while True:
    if i <= num:
        sum = sum * i
    else:
        break
    i += 1
print(sum)

def factorial(n):
    if n == 0 or n == 1:   # 終止條件，以結束遞迴
        return 1
    else:
        return n * factorial(n-1)  # 遞迴，呼叫自己

num = int(input("請輸入一個正整數進行運算："))
result = factorial(num)
print(f"{num}! = {result}")

# 7. 實作練習
# 7.1 實作題1 - 國文成績
def stat(scores):
    print(f"最高分為：{max(scores)}")
    print(f"最低分為：{min(scores)}")
    print(f"總分為：{sum(scores)}")
    print("平均為：{:.2f}".format(sum(scores) / len(scores)))

scores = []
people = 1
while True:
    score = input(f"請輸入第 {people} 位同學分數：(按 Enter 結束！)：")
    if score != "":
        scores.append(int(score))
        people += 1
    else:
        print("輸入結束！")
        break
stat(scores)

# 7.2 實作題2 - 身高單位轉換
def tran(height):
    height = height * 0.3048 * 100
    return height

height = float(input("請輸入身高 (呎)："))
result = round(tran(height), 1)
print(f"你的身高為：{result} 公分")

# 7.3 實作題3 - 以十二小時制顯示現在時刻
import time as t
result = t.strftime("現在時刻： %p %I點 %M分 %S秒", t.localtime())
print(result)

from datetime import datetime
result = datetime.now().strftime("現在時刻： %p %I點 %M分 %S秒")
print(result)

# 7.4 實作題4 - 設計一個函數 reverse(n)，此函數可以反向顯示此數
def reverse(n):
    numList = [digit for digit in n]  # 將數值分別取出並放入 list中
    # print(numList)
    reverNumList = numList[::-1]  # 將 list中的數值反轉
    # print(reverNumList)
    reverNum = int("".join(reverNumList))  # 將 list中的數值合併，並將此類型從字串改為整數
    print(reverNum)

num = input("請輸入數值：")  # 此數值為字串
reverse(num)

# 7.5 實作題5 - 判斷所輸入的數值，是不是回文(Palindrome)
def isPalindrome(n):
    numList = [digit for digit in n]
    reverNumList = numList[::-1]
    if reverNumList == numList:
        return print("這是回文數")
    return print("這不是回文數")

num = input("請輸入數值：")
isPalindrome(num)

# 7.6 實作題6 - 費式數列
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("下列是前10個Fibonacci數列")
for n in range(10):
    print(fib(n), end=" ")
