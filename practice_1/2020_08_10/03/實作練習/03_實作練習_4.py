# 實作練習_4
salary = 150
hour = int(input("請輸入本週工作時數:"))  # 20 40 45 60
if hour > 50:
    print("本週薪資:", salary * hour * 1.6)
elif hour < 50 and hour > 40:
    print("本週薪資:", salary * hour * 1.2)
elif hour == 40:
    print("本週薪資:", salary * hour )
else:
    print("本週薪資:", salary * hour * 0.8 )
