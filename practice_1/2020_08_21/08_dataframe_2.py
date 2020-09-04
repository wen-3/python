# 找出Money為500以上的人
attri_data1 = {'ID':['1','2','3','4','5'], 'Sex':['F','F','M','M','F'], 'Money':[1000,2000,500,300,700],
'Name':['Saito','Horie','Kondo','Kawada','Matsubara']}
attri_data_frame1 = DataFrame(attri_data1)
attri_data_frame1['Money'] > 500

# 分別計算男女(MF分開看)的平均Money
attri_data_frame1.groupby('Sex')['Money'].mean()

# 設置另一個dataframe
attri_data2 = {'ID':['3','4','7'], 'Math':[60,30,40], 'English':[80,20,30]}
attri_data_frame2 = DataFrame(attri_data2)
print(attri_data_frame2)

# 合併
attri_data_merge = pd.merge(attri_data_frame1, attri_data_frame2)
print(attri_data_merge)

# groupby的使用
attri_data_merge.groupby('ID')['Money','Math','English'].mean()

