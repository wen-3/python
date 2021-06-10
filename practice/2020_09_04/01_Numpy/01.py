import pandas as pd
student_data_por = pd.read_csv('student-por.csv',sep=';')
student_data_por.describe()
# student_data_por.columns  # 讀取欄位

student_data_math = pd.read_csv('student-mat.csv',sep=';')
# 未打完
student_data_merge = pd.merge(student_data_math, student_data_por, on = ['school', 'sex', 'age', 'address','famsize'], suffixes = ('_math', '_por'))
student_data_merge.describe()

# sns.pairplot(student_data_merge[['Medu', 'Fedu', 'G3_math']])
# plt.grid(True)

