import pandas as pd
from sklearn import linear_model

student_data_por = pd.read_csv('student-por.csv',sep=';')

reg = linear_model.LinearRegression()
X = student_data_por.loc[:, ['G1']].values
Y = student_data_por['G3'].values

reg.fit(X, Y)
print('迴歸係數:', reg.coef_)
print('截距:', reg.intercept_)
print('決定係数:', reg.score(X, Y))
