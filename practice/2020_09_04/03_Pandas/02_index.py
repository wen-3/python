import numpy as np
import pandas as pd
from pandas import Series, DataFrame

hier_df1 = DataFrame(
np.arange(12).reshape((3,4)),
index = [['c','d','d'],[1,2,1]],
columns = [
    ['Kyoto','Nagoya','Hokkaido','Kyoto'],
    ['Yellow','Yellow','Red','Blue']
    ]
)
hier_df1.index.names = ['key1','key2']
hier_df1.columns.names = ['city','color']
hier_df1   # 執行

hier_df1['Kyoto']

hier_df1.mean(level='city', axis=1)

hier_df1.sum(level='key2')
