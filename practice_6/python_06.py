# dict
fruits = {"西瓜":15, "香蕉":20, "水蜜桃":25}
noodles = {"牛肉麵":100, "肉絲麵":80, "陽春麵":50}
print(fruits)
print(noodles)

fruits["香蕉"] = 12  # 修改
print(fruits)
fruits["橘子"] = 18  # 新增
print(fruits)

# 血型個性查詢
dict1 = {"A":"活潑", 
         "B":"外向樂觀",
         "O":"自信堅強",
         "AB":"內向"}

name = input("輸入要查詢的血型:")
blood = dict1.get(name)
if blood == None:
    print("沒有「" + name + "」血型!")
else:
    print( name + "血型的個性為：" + blood)


# 天氣型態
dict1 = {"春季":"暖和", 
         "夏季":"炎熱",
         "秋季":"涼爽",
         "冬季":"寒冷"}

season = input("輸入季節名稱:")
weather = dict1.get(season)
if weather == None:
    print("沒有「" + season + "」季節!")
else:
    print( season + "的天氣為 " + weather)


# 輸入及查詢學生成績
dict1 = {"林小明":85, 
         "曾山水":93, 
         "鄧美麗":67}

name = input("輸入學生姓名：")
if name in dict1:
    print(name + "的成績為" + str(dict1[name]))
else:
    score = input("輸入學生分數：")
    dict1[name] = score
    print("字典內容:" + str(dict1))


# 電器經銷商查詢各電器的價格
dict1 = {"電視":15000,
         "冰箱":23000, 
         "冷氣":28000}

name = input("輸入電器名稱：")
if name in dict1:
    print(name + "的價格為" + str(dict1[name]))
else:
    price = input("輸入電器價格：")
    dict1[name] = price
    print("字典內容:" + str(dict1))

# 顯示世大運獎牌數
dict1 = {"金牌":26, 
         "銀牌":34, 
         "銅牌":30}

listKey = list(dict1.keys())
listValue = list(dict1.values())
for i in range(len(listKey)):
    print("得到的 %s 數目為 %d 面" %(listKey[i], listValue[i]))

  # 另一寫法
    dict1 = {"金牌":26, 
            "銀牌":34, 
            "銅牌":30}

    item1 = dict1.items()
    for name, num in item1:
        print("得到的 %s 數目為 %d 面" %(name, num))

# 星座名稱及性格特徵
dict1 = {"水瓶座":"活潑善變", 
         "雙魚座":"迷人保守", 
         "白羊座":"天生勇者",
         "金牛座":"熱情敏感"}

listKey = list(dict1.keys())
listValue = list(dict1.values())
for i in item1:
    print("%s 的性格特徵為 %s" %(listKey[i],listValue[i]))

  # 另一寫法
    dict1 = {"水瓶座":"活潑善變", 
            "雙魚座":"迷人保守", 
            "白羊座":"天生勇者",
            "金牛座":"熱情敏感"}

    item1 = dict1.items()
    for name, nature in item1:
        print("%s 的性格特徵為 %s" %(name, nature))

# 麵價格排序
noodles = {"牛肉麵":100, 
          "肉絲麵":80, 
          "陽春麵":60,
          "大滷麵":90,
          "麻醬麵":70}
print(noodles)

noodlesList = sorted(noodles.items(), key = lambda item:item[1])
print(noodlesList)
type(noodlesList)

# 小兵字典
import numpy as np
armys = []      # 建立小兵空串列
for soldier_number in range(50):   # for_ in range(50)
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)

for soldier in armys[:3]:     # 列印前3個小兵
    print(soldier)

print("小兵數量 = ", len(armys))     # 列印小兵數量

for soldier_number in range(50):
    random_num = np.random.rand()      # 產生 0~1 的隨機變數
    temp_soldier = armys[soldier_number]      # generate a list by index soldier_number
    if random_num >= 0.5:
        temp_soldier["tag"] = 'red'     # update temp_soldier's tag
    else:
        temp_soldier["tag"] = 'blue'
for soldier in armys[:3]:
    print(soldier)
