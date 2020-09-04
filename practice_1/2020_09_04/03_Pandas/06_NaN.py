# 資料的準備
import numpy as np
from numpy import nan as NA
import pandas as pd
df2 = pd.DataFrame(np.random.rand(15,6))
# 設定為NA
df2.iloc[2,0] = NA
df2.iloc[5:8,2] = NA
df2.iloc[7:9,3] = NA
df2.iloc[10,5] = NA
df2

df2.dropna()  # 刪除 NaN

df2.fillna(0)  # 將NaN以0來填補

df2.fillna(df2.mean()) # 將NaN分別以各行的平均值來填補
