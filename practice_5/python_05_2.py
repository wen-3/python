# 學生成績排序
scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if inscore=="":
        break
    scores.append(int(inscore))

scores2 = sorted(scores, reverse = False)
print("成績由小到大的排序：", scores2)    

# 練習一
numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]
odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print(odd_numbers)

# 練習二
numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]
odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        if number not in odd_numbers:
            odd_numbers.append(number)
print(odd_numbers)

# 練習三
fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束)：")
    if fruit == "":
        break
    if fruit in fruits:
        n = fruits.index(fruit)  # 找水果的索引直
        print(fruit,"在串列中的第", n+1 ,"項")
    else:
        print(fruit,"不再串列中")


# 練習四
# 找出成績最高分的同學，並顯示其姓名與成績 
names = []
scores = []
for i in range(3):
    inname = input("請輸入第" + str(i+1) + "同學的姓名：")
    inscore = input("請輸入第" + str(i+1) + "同學的成績：")
    names.append(inname)
    scores.append(inscore)
max_scores = max(scores)
max_index_name = scores.index(max(scores))
print("姓名：",names[max_index_name],"  成績：", max_scores)

