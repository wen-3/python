import numpy as np
import pandas as pd
from pandas import Series, DataFrame
hier_df = DataFrame(
    np.arange(9).reshape((3,3)),
    index = [
        ['a','a','b'],
        [1,2,2]
    ],
    columns = [
        ['Osaka','Tokyo','Osaka'],
        ['Blue','Red','Red']
    ]
)
hier_df


# 對index附加名稱
hier_df.index.names =['key1','key2']
# 對columns附加名稱
hier_df.columns.names =['city','color']
hier_df
hier_df['Osaka']

