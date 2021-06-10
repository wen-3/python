import pandas as pd
from pandas import Series, DataFrame
student_data_math = pd.read_csv('student-mat.csv', sep=';')
add_age = student_data_math['age'] * 2
student_data_math['add_age'] = add_age
student_data_math.head()
# 範例用 lambda
