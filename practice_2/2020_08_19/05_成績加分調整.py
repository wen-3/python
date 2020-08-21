# 成績加分調整
# 加10分
# 加分上限為90
# 原始分數大於90的不變
scores = [30,99,41,55,84,72]
scores_new = []

n = len(scores)
for i in range(0, n):
    if scores[i] > 90:
        scores_new.append(scores[i])
    else:
        scores[i] += 10
        if scores[i] >= 90:
            scores[i] = 90
        scores_new.append(scores[i])
print("成績加分的結果為:", scores_new)   
