import pandas as pd
from pandas import Series, DataFrame
student_data_math = pd.read_csv('student-mat.csv', sep=';')
student_data_math.groupby(['school'])['G1'].mean()
student_data_math.head()


student_data_math.groupby(['school','sex'])['G1','G2','G3'].mean()
student_data_math.head()
