# 加入此行，避免中文字讀取失敗
# -*- coding:utf-8 -*-

# 1. 檔案的操作
# 1.1 以寫入模式開啟檔案並寫入資料 - open函式
f = open("Ch9_FileAndException/file1.txt", "w", encoding="utf-8")
content = "Hello Python\n中文字測試\nWelcome"
f.write(content)
f.close

# 1.2 以讀取模式開啟檔案並顯示資料 - open函式
f = open("Ch9_FileAndException/file1.txt", "r", encoding="utf-8")
print(f.read())
f.close

# 1.3 以 with...as 語法開啟檔案並顯示資料
with open("Ch9_FileAndException/file1.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 1.4 在每段文章的前面加上編號 - readlines() 方法
content = """串列(又稱為「清單」或「列表」，與其他語言的「陣列 (Array)」)相同，其功能與變數相類似，是提供儲存資料的記憶體空間。\n每一個串列擁有一個名稱，做為識別該串列的標誌；串列中每一個資料稱為「元素」，每一個串列元素相當於一個變數。\n可以把串列想成是有許多相同名稱的箱子，連續排列在一起，而每個箱子有不同編號，只要指定編號即可存取對應箱子內的資料。"""
path = "Ch9_FileAndException/file3.txt"

# 使用 with...as
with open(path, "w", encoding="utf-8") as f:    # 先判斷檔案是否存在，不存在，就創建檔案；存在，清空檔案裡的內容
    f.write(content)   # 寫入資料。(覆寫)
with open(path, "r", encoding="utf-8") as f:     # 讀取檔案，預設為讀取
    lines = f.readlines()    #　逐行讀取，並放進 list中
with open(path, "w", encoding="utf-8") as f:
    count = 0
    for line in lines:
        count += 1
        newLine = f"{count}：{line}"
        f.write(newLine)    # 寫入資料。(覆寫)

# 使用 open()
f = open(path, "w+", encoding="utf-8")
f.write(content)
f.close

f = open(path, encoding="utf-8")
lines = f.readlines()
f.close

f = open(path, "w+", encoding="utf-8")
count = 0
for line in lines:
    count += 1
    newLine = f"{count}：{line}"
    f.write(newLine)
f.close

# 1.5 開啟文字檔<file1.txt>，以read()方法讀取後計算文章中總共有幾個字元
path = "Ch9_FileAndException/file1.txt"
with open(path, encoding="utf-8") as f:
    content = f.read()
    print(len(content))

# 2. 例外處理
# 2.1 輸入兩個正整數求和，捕捉輸入的錯誤 - try...except
try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a + b
    print("r=", r)   
except:
    print("發生輸入非數值的錯誤！")

# 2.2 以 open函式開啟檔案並顯示其內容，讓程式處理當輸入檔案不存在或檔案開啟錯誤時，可以以 try…except捕捉發生的錯誤
try:
    path = input("請輸入想開啟的檔案路徑：")
    f = open(path, encoding="utf-8")
    print(f.read())
    f.close
except:
    print("輸入檔案不存在或檔案開啟錯誤")

# 2.3 捕捉非數值資料和餘數為 0 的錯誤 - try...except
try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a % b
    print("餘數為", r)
except ValueError:
    print("發生輸入非數值的錯誤！")
except ZeroDivisionError:
    print("發生 integer division or modulo by zero 的錯誤，包括分母為0的錯誤！")
finally:
    print("一定會執行的程式區塊")

# 2.4 輸入兩個正整數，求兩數相除，以try…except捕捉發生的錯誤，包括輸入非數值和除數為0的錯誤
try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數："))
    r = a / b
    print("商為", r)
except ValueError:
    print("發生輸入非數值的錯誤！")
except ZeroDivisionError:
    print("發生除數為0的錯誤！")
finally:
    print("一定會執行的程式區塊")

# 3. 實作練習
# 3.1 實作題1 - 以readlines()函式讀取文字檔<in_a.txt>，計算每一列的字元數(包含結束字元)，並在每一列前面顯示
content = """Asdf j213k as kfjas 932kk s8aklsd\nAsd klfj 823kjds\n23ksad f9ksdaf\nasdfj89as df8kasdf"""

path = "Ch9_FileAndException/file5.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

with open(path) as f:
    for line in f:
        print(f"字元數={len(line)}：{line}")

# 3.2 實作題2 - 以read()函式讀取文字檔<in_a.txt>，並統計出文章中共有幾個英文字母A(包含A或a)
path = "Ch9_FileAndException/file5.txt"

# 3.2.1 利用 String Method()
with open(path) as f:
    allContent = f.read().lower()
    countWord = allContent.count("a")
    print(f"文章中共有 {countWord} 個英文字母A(包含A或a)！")

# 3.2.2 利用迴圈搜尋
with open(path) as f:
    allContent = f.read()
    time = 0
    for ch in allContent:
        if ch == "A" or ch == "a":
            time += 1
    print(f"文章中共有 {time} 個英文字母A(包含A或a)！")

# 3.3 實作題3 - 輸入正整數n後，可以顯示1, 2, …, n數列的程式，以try…excep加入錯誤的捕捉 (非數值的錯誤)
try:
    n = int(input("請輸入正整數 n："))
    for num in range(1,n+1):
        print(num, end=" ")
except ValueError:
    print("發生輸入非數值的錯誤！")
