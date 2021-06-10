# 1. dict.get()
# 1.1 血型個性查詢dict.get()
dictBlood = {"A":"活潑", 
             "B":"外向樂觀",
             "O":"自信堅強",
             "AB":"內向"}

inblood = input("輸入要查詢的血型：")
bloodValue = dictBlood.get(inblood)
if bloodValue == None:
    print(f"沒有「{inblood}」血型!")
else:
    print( f"{inblood} 血型的個性為：{bloodValue}")

# 1.2 天氣型態
dictSeason = {"春季":"暖和", 
               "夏季":"炎熱",
               "秋季":"涼爽",
               "冬季":"寒冷"}

inSeason= input("輸入季節名稱：")
weatherValue = dictSeason.get(inSeason)
if weatherValue == None:
    print(f"沒有「{inSeason}」季節!")
else:
    print( f"{inSeason}的天氣為 {weatherValue}")

# 2. in 功能
# 2.1 輸入及查詢學生成績
dictStudent = {"林小明":85, 
               "曾山水":93, 
               "鄧美麗":67}

inName = input("輸入學生姓名：")

if inName in dictStudent:
    print(f"{inName}的成績為 {dictStudent[inName]}")
else:
    inScore = int(input("輸入學生分數："))
    dictStudent[inName] = inScore
    print(f"字典內容：{dictStudent}")

# 2.2 電器經銷商查詢各電器的價格
dict1 ={"電視":15000,
        "冰箱":23000, 
        "冷氣":28000}

inElec = input("輸入電器名稱：")

if inElec in dict1:
    print(f"{inElec}的價格為 {dict1[inElec]}")
else:
    inPrice = int(input("輸入價格："))
    dict1[inElec] = inPrice
    print(f"字典內容：{dict1}")

# 3. keys 及 values
# 3.1 顯示世大運獎牌數
dict1 = {"金牌":26, 
         "銀牌":34, 
         "銅牌":30}

for key in dict1.keys():
    print(f"得到的 {key} 數目為 {dict1[key]} 面")

# 使用 items()
for key, value in dict1.items():
    print(f"得到的 {key} 數目為 {value} 面")

# 3.2 星座名稱及性格特徵
dict1 = {"水瓶座":"活潑善變", 
         "雙魚座":"迷人保守", 
         "白羊座":"天生勇者",
         "金牛座":"熱情敏感"}

for key in dict1.keys():
    print(f"{key} 的性格特徵為 {dict1[key]}")

# 使用 items()
for key, value in dict1.items():
    print(f"{key} 的性格特徵為 {value}")

# 4. 依值排序與遍歷字典的值
# 4.1 麵價格排序
noodles = {"牛肉麵":100, 
          "肉絲麵":80, 
          "陽春麵":60,
          "大滷麵":90,
          "麻醬麵":70}

newNoodles = sorted(noodles.items(), key=lambda item : item[1])
print(newNoodles)
print(type(newNoodles))

# 小兵字典 - 額外補充
# import numpy as np
# armys = []      # 建立小兵空串列
# for soldier_number in range(50):   # for_ in range(50)
#     soldier = {'tag':'red', 'score':3, 'speed':'slow'}
#     armys.append(soldier)

# for soldier in armys[:3]:     # 列印前3個小兵
#     print(soldier)

# print("小兵數量 = ", len(armys))     # 列印小兵數量

# for soldier_number in range(50):
#     random_num = np.random.rand()      # 產生 0~1 的隨機變數
#     temp_soldier = armys[soldier_number]      # generate a list by index soldier_number
#     if random_num >= 0.5:
#         temp_soldier["tag"] = 'red'     # update temp_soldier's tag
#     else:
#         temp_soldier["tag"] = 'blue'
# for soldier in armys[:3]:
#     print(soldier)

# 5. 實作練習
# 5.1 實作題1 - 六都的 PM2.5
city = {"台北市": 6,
        "新北市": 2,
        "桃園市": 5,
        "台中市": 8,
        "台南市": 3,
        "高雄市": 9}

inCity = input("輸入要查詢的六都名稱：")
PM_value = city.get(inCity)

if PM_value == None:
    print(f"六都中沒有「{inCity}」城市！")
else:
    print(f"{inCity} 今天的 PM2.5 值為：{PM_value}")

# 5.2 實作題2 - 不同生肖的性格特徵 - 使用items
dict1 = {"鼠":"親切和藹",
         "牛":"保守努力",
         "虎":"熱情大膽",
         "兔":"溫柔仁慈"}

for k, v in dict1.items():
    print(f"生肖屬 {k} 的性格特徵為 {v}")

# 5.3 實作題3 - 水果的每斤售價 - 依水果名排序列印
fruits = {"Watermelon":15,
          "Banana":20,
          "Pineapple":25,
          "Orange":12,
          "Apple":18}

print(fruits)
print(type(fruits))
print()

newFruits = sorted(fruits.items(), key=lambda item:item[0])
print(newFruits)
print(type(newFruits))
print()

newFruits = dict(newFruits)
for item in newFruits.keys():
    print(f"{item}：{newFruits[item]}")
print(type(newFruits))

# 5.4 實作題4 - 麵的售價
noodles = {'牛肉麵':100,
           '肉絲麵':80,
           '陽春麵':60,
           '大滷麵':90,
           '麻醬麵':70}

print(noodles)
newNoodles = sorted(noodles.items(), key=lambda item:item[1])
newNoodles = dict(newNoodles)
for item in newNoodles.keys():
    print(f"{item}：{newNoodles[item]}")

maxKey = max(noodles, key=noodles.get)
minKey = min(noodles, key=noodles.get)
maxValue = max(noodles.values())
minValue = min(noodles.values())
print(f"最貴的是  {maxKey} 金額是 {maxValue}")
print(f"最便宜的是 {minKey} 金額是 {minValue}")
