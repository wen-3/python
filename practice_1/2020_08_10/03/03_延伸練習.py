# 電影依年齡分級
age = int(input("請輸入年齡："))  # 5 10 17 21
if age >= 18:
    print("您已成年，可看各級影片")
elif age >= 12 and age < 18:
    print("可看限制級以外所有影片")
elif age >= 6 and age < 12:
    print("可看普遍級及保護級")
else:
    print("可看普遍級")
