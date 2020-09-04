import pandas as pd
from pandas import Series, DataFrame

# Series
attri_data1 = {'ID':['100','101','102','103','104'],
'City':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
'Birth_year':[1990,1989,1992,1997,1982],
'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}
attri_data_frame1 = DataFrame(attri_data1)
print(attri_data_frame1)

print()

# 可變更索引值為文字。
attri_data_frame_index1 = DataFrame(attri_data1,index=['a','b','c','d','e'])
print(attri_data_frame_index1)

print()
# 轉置
print(attri_data_frame_index1.T)

print()
# 取出特定某一行
print(attri_data_frame_index1.Birth_year)

print()
# 取出特定多行
print(attri_data_frame_index1[['ID', 'Birth_year']])

# 條件篩選
print()
print(attri_data_frame_index1['City']=='Tokyo')

print()
print(attri_data_frame_index1['Birth_year']<1990)

# 要刪除某個特定的行或列
attri_data_frame_index1.drop(['Birth_year'], axis = 1)

# 設置另一個dataframe
attri_data2 = {'ID':['100','101','102','105','107'], 'Math':[50,43,33,76,98], 'English':[90,30,20,50,30], 'Sex':['M','F','F','M','M']}
attri_data_frame2 =DataFrame(attri_data2)
attri_data_frame2

# 資料的合併（內部結合）
pd.merge(attri_data_frame_index1,attri_data_frame2)

# groupby的使用
attri_data_frame2.groupby('Sex')['Math'].mean()
attri_data_frame2.groupby('Sex')['English'].mean()

