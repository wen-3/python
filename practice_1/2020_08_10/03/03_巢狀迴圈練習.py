# 巢狀迴圈練習(找出數字最大的數字)
a = int(input("請輸入第一個數:"))
b = int(input("請輸入第二個數:"))
c = int(input("請輸入第三個數:"))

# 自身寫法
num = a
if num <= b:
    num = b
    if num <= c:
        num = c
else:
    if num <= c:
        num = c
print("最大值:",num)

# 老師寫法
if a>b:
    if a>c:
        print("最大值為",a)
    else:
        print("最大值為",c)
else:
    if b>c:
        print("最大值為",b)
    else:
        print("最大值為",c)