# 串列資料結構
score = []
total = inscore = 0
while(inscore != -1):
    inscore = int(input("請輸入學生的成績："))
    score.append(inscore)
print("共有 %d位學生" %(len(score)-1))

for i in range(0, len(score)-1):
    total += score[i]
average = total / (len(score)-1)
print("班上同學成績為：",score[0:len(score)-1])
print("本班總成績：%d 分，平均成績：%.2f分" %(total, average))
