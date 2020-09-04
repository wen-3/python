import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

student_data_por = pd.read_csv('student-por.csv',sep=';')

reg = linear_model.LinearRegression()
X = student_data_por.loc[:, ['absences']].values
Y = student_data_por['G3'].values

reg.fit(X, Y)
print('迴歸係數:', reg.coef_)
print('截距:', reg.intercept_)
print('決定係数:', reg.score(X, Y))
# 散佈圖
plt.scatter(X, Y)
plt.xlabel('absences')
plt.ylabel('G3 grade')

# 線性迴歸直線
plt.plot(X, reg.predict(X))
plt.grid(True)
