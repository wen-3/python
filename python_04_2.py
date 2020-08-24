# 練習
num = 0
answer = 36
while (num != answer):
    num = int(input("請輸入1~100的數字"))
    if num > answer:
        print("請猜小一點")
    elif num < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")

# 練習
xlst = [n for n in range(1,100,2)]

# 1
sum = 0
for n in range(1,100,2):
    sum += n
print(sum)

# 2
for i in range(2,10):
    for j in range(1,10):
        num = i * j
        print("%d*%d=%2d" %(i,j,num),end = " ")
    print()

# 3
num = int(input("請輸入正整數"))
for i in range(1,num+1):
    for j in range(i,num+1):
        print("*",end="")
    print()

# 3(另一種寫法)
num = int(input("請輸入正整數"))
for i in range(num,0,-1):
    print("*"*i)
print()

# 4
num = int(input("請輸入正整數"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        print(i,end=" ")
        count+=1
print("%d的因數有"%(num),end=" ")
print()

if count>2:
    print("%d不是質數"%(num))  
else:
    print("%d是質數"%(num))

# 5
weight = 50
for i in range(1,6):
    weight += 1.2
    print("第 %d 年體重：%.1f" %(i,weight))

# 6
for i in range(10,101,10):
    n = 1
    e = 1
    for j in range(1,i+1):
        n *= j
        e += (1 / n)
    print("當i是%3d時 e = %.39f" %(i,e))

# 6 範例
e=1
val = 1
for i in range(1,101):
    val = val / i
    e += val   
    if i % 10 ==0:
        print("當i是%3d時 e= %.39f" % (i, e))

# 6(另一種寫法)
import numpy
n = 1
for i in range(1,101,1):
    n += 1/numpy.math.factorial(i)
    if (i%10)==0:
        print(f"當i是 {i:3d} 時 e = {n:2.39f}")

