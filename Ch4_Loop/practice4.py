# 1. range 函式
# 1.1 以 range 函式建立數列
list1 = range(0, 10)
list2 = range(1, 10)
list3 = range(1, 10, 2)
list4 = range(10, 1, -2)

print(list1)
print(list2)
print(list3)
print(list4)

# 2. for迴圈
# 2.1 顯示正整數數列
num = int(input("請輸入正整數："))
for i in range(1, num+1):
    print(i, end=" ")

# 2.2 計算正整數總和
num = int(input("請輸入正整數："))
sum = 0
for i in range(1, num+1):
    sum += i

print("1 到 {} 的整數和為 {}".format(num, sum))

# 2.3 延伸練習 - 利用range顯示由1到該整數的所有奇數
num  = int(input("請輸入正整數："))
for i in range(1, num+1, 2):
    print(i, end = " ")

# 2.4 巢狀 for迴圈
# 2.4.1 井字直角三角形
j = 0
for i in range(1, 6):
    print("外部執行第 {0} 次迴圈, 內部執行 {1} 次迴圈：".format(i, j+1), end = " ")
    for j in range(1, i+1):
        print("#", end="")
    print()
    
# 2.4.2 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print("{}*{}={:2d}".format(i, j, i*j), end=" ")
    print()

# 2.4.3 進階延伸 - 自行補充
# 2.4.3.1
num = int(input("請輸入一個正整數："))
for i in range(1, 6):
    print("{}*{}={:2d}".format(num, i, num*i))
    if i != 5:
        print("{}*{}={:2d}".format(num, (10 - i), num*(10 - i)))

# 2.4.3.2
for i in range(1, 10):
    for j in range(1, 6):
        print("{}*{}={:2d}".format(i, j, i*j), end = " ")
        if j != 5:
            print("{}*{}={:2d}".format(i, (10 - j), i*(10 - j)), end = " ")
    print()

# 2.4.4 延伸練習 - 三角形數字排列
n = int(input("請輸入正整數："))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()

# 3. break 命令 - 找最小公倍數
a = int(input("請輸入 a 的值："))
b = int(input("請輸入 b 的值："))

for i in range(2, 10):
    if a % i == 0 and b % i == 0:
        gcd = i
        break 

lcm = int((a * b) / gcd)
print("{} 和 {} 的最小公倍數 = {}".format(a, b, lcm))

# 4. continue 命令 - 顯示正整數數列，排除 5的倍數
num = int(input("請輸入正整數："))
for i in range(1, num+1):
    if(i % 5 == 0):
        continue
    print(i, end=" ")

# 4.1 幫樓層命名 - 避開 4這個樓層
floor = int(input("請輸入大樓的樓層數："))
print("本大樓具有的樓層為：")
for i in range(1, floor+1+1):
    if(i==4):
        continue
    print("{}".format(i), end=" ")

# 5. while 迴圈
# 5.1 while 迴圈計算 n!
n = int(input("請輸入正整數 n 的值："))
i = total = 1

while(i <= n):
    total *= i
    i += 1
print(f"{n}!={total}")

# 5.2 猜數字遊戲
answer = int(input("請輸入1-100間的數字："))

while(True):
    guess = int(input("請猜1-100間的數字 = "))
    if guess == answer:
        print("恭喜答對了")
        break
    else:
        if guess > answer:
            print("請猜小一點")
        else:
            print("請猜大一點")

# 5.3 延伸練習 - 輸入一個正整數後，顯示由1到該整數的所有偶數
n = int(input("請輸入正整數 n 的值："))
i = 2

while(i <= n):
    if i % 2  == 0:
        print(i, end=" ")
    i += 1

# 6. 實作練習
# 6.1 實作題1 - 建立一個1, 3, …, 99的奇數數列。並以for迴圈計算該數列的總和
sum = 0
for i in range(1, 100, 2):
    sum += i

print(sum)

# 6.2 實作題2 - 利用for巢狀迴圈列出由2開始的九九乘法表
for i in range(2, 10):
    for j in range(2, 10):
        print("{}*{}={:2d}".format(i, j, i*j), end = " ")
    print()

# 6.3 實作題3 - 輸入一個正整數，程式會顯示由1到該整數的倒三角形
n = int(input("請輸入正整數："))
for i in range(1, n+1):
    for j in range(i, n+1):
        print("*", end="")
    print()

# 6.3.1 進階延伸 - 金字塔
# n = int(input("請輸入正整數："))

# 6.4 實作題4 - 輸入一正整數，列出此數的所有正因數，並判斷此數字是否為質數
# n = int(input("請輸入正整數："))
time = 0
print(n, "的因數有", end=" ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        time += 1
print() 
if time > 2:
    print(n, "不是質數")
else:
    print(n, "是質數")

# 6.5 實作題5 - 假設你今年體重是50公斤，每年可以增加1.2公斤，請列出未來5年的體重變化
weight = 50
add = 1.2
for i in range(1, 6):
    weight += add
    print("第 {} 年體重：{:.1f}".format(i, weight))

# 6.6 實作題6 - 歐拉數
for i in range(1,101):
    e = 1
    n = 1
    for j in range(1,i+1):
        n *= j
        e += (1 / n)
    if i % 10 == 0:
        print("當i是{:3d}時 e = {:.39f}".format(i, e))

# 6.6.1 其他寫法
e=1
val = 1
for i in range(1,101):
    val = val / i
    e += val   
    if i % 10 ==0:
        print("當i是%3d時 e= %.39f" % (i, e))

# 6.6.2 其他寫法
import numpy
n = 1
for i in range(1,101,1):
    n += 1/numpy.math.factorial(i)
    if (i%10)==0:
        print(f"當i是 {i:3d} 時 e = {n:2.39f}")
