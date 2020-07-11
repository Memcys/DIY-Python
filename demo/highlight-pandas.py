# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# # %pip install -U pandas
# # %pip install -U openpyxl xlrd    # for to_excel and read_excel with .xlsx
# # %pip install -U matplotlib    # for plot
# # %pip install -U scipy    # for 'kde' in pandas.plotting.scatter_matrix
# -

# - [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
# - [pandas 速览](https://pandas.pydata.org/docs/getting_started/index.html)
# - [10 minutes to pandas](https://pandas.pydata.org/docs/getting_started/10min.html#min)

# # 数据列表

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ## 数据列 [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)

s = pd.Series([1, 3, 5, pd.NA, 8, 10, 12])
s

# ## 数据表 ([DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame))

df = pd.DataFrame(np.random.randn(60, 40))
df

df.head()

df.tail()

df.describe()

# ### 选择

df[3]    # 选择第 4 列

df[0:2]    # 选择第 1 至 第 2 列

# 整数索引 `iloc`

df.iloc[0, 2]    # 选择第 1 行 第 3 列

df.iloc[1, :3]    # 选择第 2 行前 3 列

# 选择单个元素推荐用 `at` 或 `iat`

# %timeit df.iloc[0, 2]
# %timeit df.at[0, 2]    # 快于 df.iloc[0, 2]

# 布尔索引

df[df > 0]

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
df2

df2.loc[1, 'E']

# ## 导出

df2.to_csv('../data/AF.csv')
df2.to_excel('../data/AF.xlsx')

# 查看当前文件夹下名称以 'AF.' 开头的文件

sorted(Path('../data/').rglob('AF.*'))

# ## 导入

df3 = pd.read_excel('../data/AF.xlsx', sheet_name='Sheet1', index_col=0)
df3

# ## 可视化

dfcs = df.loc[:, :5].cumsum()
dfcs.plot()

df.plot.scatter(x=0, y=1, s=df[2] * 50, c=3)

df.loc[:, :3].plot.hist(alpha=.25)

df.loc[:, :5].plot.box()

df.plot.hexbin(x=2, y=3, gridsize=10)

df.loc[:3, :1].abs().plot.pie(subplots=True)

pd.plotting.scatter_matrix(df.loc[:, :3],diagonal='kde')

pd.plotting.lag_plot(df[0])

# +
fig, ax = plt.subplots()

df4 = df.loc[:4, :3]
pd.plotting.table(ax, df4.describe(), loc='top')
df4.plot(ax=ax, legend=None)

# +
plt.figure()

df5 = df.loc[:, 5]
df5.plot()
plt.fill_between(range(len(df5)), df5 - 5 * df.loc[:, 4].abs(), df5 + 5 * df.loc[:, 6].abs(), color='b', alpha=.25)
