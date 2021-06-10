# Lecture_04_1
#1) 請使用Scipy，計算使得下面的函數為0的解
#   f(x)=5*x-10
from scipy.optimize import fsolve
def f(x):
    y = 5 * x - 10
    return y

x = fsolve(f,0)
print(x)

# Lecture_04_2
#2) 同上題，請計算使得下面的函數為0的解
f(x)=x**3-2*x**2-11*x+12
from scipy.optimize import fsolve
def f(x):
    y = x ** 3 - 2 * x ** 2 - 11 * x + 12
    return y

x = fsolve(f,0)
print(x)

# Lecture_05_1
# a) 對於上述資料，以年齡(age)配上性別(sex)來計算出G1的平均分數，製作縱軸為年齡(age)、橫軸為(sex)的表(Table)
import requests, zipfile
from io import StringIO
import io
import pandas as pd

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00356/student.zip'
r = requests.get(url, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

student_data_math = pd.read_csv('student-mat.csv',sep = ";")
student_data_math.head()

new_student_data_math = pd.pivot_table(student_data_math,index = 'age',columns = 'sex', values = 'G1', aggfunc = 'mean')
print(new_student_data_math)

# Lecture_05_2
# b) 對於問題(a)顯示的結果Table，顯示將有著NaN之列（紀錄）全部刪除之後的結果
new_student_data_math.dropna()
