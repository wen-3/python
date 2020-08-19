# 計算正整數的總和
sum = 0
n = int(input("請輸入正整數："))
for i in range(1, n+1):
    sum+=i
print("1到%d的整數和為%d" %(n, sum))