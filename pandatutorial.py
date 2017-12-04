# -*- coding: utf-8 -*-
"""
@author: Kanika
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

"""
Commands used on this dataframe:
    
    1. df2.dtypes
    2. df.head()
    3. df.tail(3)
    4. df.index - Display the index, columns, and the underlying numpy data
    5. df.values
    6. df.describe() - Describe shows a quick statistic summary of your data
    7. df.T - Transposing data
    8. df.sort_index(axis=1, ascending=False) - sorting by axis
    9. df.sort_values(by='B')  Sorting by values
    10. df.loc[dates[0]] - For getting a cross section using a label 
    11. df.loc[:,['A','B']] - Selecting on a multi-axis by label
    12. df.loc['20130102':'20130104',['A','B']] - Showing label slicing, both endpoints are included
    13. df.loc['20130102',['A','B']] - Reduction in the dimensions of the returned object
     
    and so on.
    Refer to http://pandas.pydata.org/pandas-docs/stable/10min.html
    
"""
