# dict
fruits = {"西瓜":15, "香蕉":20, "水蜜桃":25}
noodles = {"牛肉麵":100, "肉絲麵":80, "陽春麵":50}
print(fruits)
print(noodles)

fruits["香蕉"] = 12  # 修改
print(fruits)
fruits["橘子"] = 18  # 新增
print(fruits)


# 天氣型態
dict1 = {"春季":"暖和", 
         "夏季":"炎熱",
         "秋季":"涼爽",
         "冬季":"寒冷"
        }
season = input("輸入季節名稱:")
weather = dict1.get(season)
if weather == None:
    print("沒有「" + season + "」季節!")
else:
    print( season + "的天氣為 " + weather)

