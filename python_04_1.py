# range 函式
list1 = range(5)
print(list1)
print(list(list1))

# range 函式
list1 = range(10)
list2 = range(1, 10)
list3 = range(1, 10, 2)
list4 = range(10, 1, -2)
print(list(list1))
print(list(list2))
print(list(list3))
print(list(list4))


# for 迴圈 (顯示正整數的數列)
n = int(input("請輸入正整數:"))    # 7
for i in range(1, n+1):
    print(i, end=" ")     # print(i, end=",")


# for 迴圈 (顯示正整數的總和)
sum = 0
n = int(input("請輸入正整數"))   # 10
for i in range(1,n+1):
    sum+=i
print("1 到 %d 的整數和 %d" %(n, sum))
# print("1 到 {} 的整數和 {}".format(n, sum))
print(sum)


# for 迴圈 (顯示 1 到整數的奇數)
n = int(input("請輸入正整數:"))  # 30
for i in range(1, n+1,2):
    print(i, end=" ") 


# for 巢狀迴圈 (#字直角三角形)
n = 5
for i in range(1, n+1):  # 外部迴圈
    print("外部第",i,"次迴圈,內部執行",i,"次迴圈:",end = "")
    for j in range(1, i+1):  # 內部迴圈
        print("#",end = "")
    print()   # 換行



# for 巢狀迴圈 (九九乘法表)
for i in range(1, 10):
    for j in range(1, 10):
        num = i * j
       # print(i,"*",j,"=",num, end = "  ")  # 會跑版
        print("%d*%d=%2d" %(i,j,num),end=" ")  
       # print(f"{i}*{j}={num:2d}",end=" ")   # 老師作法
    print()


# for 巢狀迴圈 (1到該整數的三角形數列)
n = int(input("請輸入正整數:"))   # 8
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# for 迴圈(break)(最小公倍數)
a = int(input("請輸入 a 的值:"))
b = int(input("請輸入 b 的值:"))
maxno = a*b + 1
for i in range(max(a,b), maxno):
    if(i%a==0 and i%b==0):
        print("%d 和 %d 最小公倍數=%d" %(a, b, i))
        break


# for 迴圈(continue)(跳過 5 的倍數)
n = int(input("請輸入正整數:"))  # 21
for i in range(1, n+1):
    if i % 5 == 0:
        continue
    print(i, end = " ")



# for 迴圈(continue)(跳過 4 的樓層)
n = int(input("請輸入大樓樓層數:"))  # 3 10
print("本大樓具有的樓層為:")
if n > 3:
    n += 1
for i in range(1, n+1):
    if i == 4:
        continue
    print(i ,end = " ")


# for 迴圈(continue)(跳過 4 的樓層)
n = int(input("請輸入大樓樓層數:"))  # 3 10
print("本大樓具有的樓層為:")
if n < 4:
    for i in range(1, n+1):
        print(i ,end = " ")
else:
    for i in range(1, n+1+1):
        if i == 4:
            continue
        print(i ,end = " ")
print()



# while 迴圈 (計算階層)
total = i = 1
n = int(input("請輸入正整數:"))  # 5
while i<=n :
    total *= i
    i += 1
print("%d!=%d" %(n, total))

