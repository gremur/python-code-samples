import pandas as pd
import numpy as np

df = pd.DataFrame()

# GROUP_BY
# group rows by columns 'column_name_1' and 'column_name_2'
# aggregate data in columns 'column_name_3' and 'column_name_4'
# aggregate data by count, mean and median
(df.groupby(['column_name_1', 'column_name_2'])
 [['column_name_3', 'column_name_4']]
 .agg({'column_name_3': ['count', 'mean'], 'column_name_4': ['mean', 'median']}))


# group rows by columns 'column_name_1'
# aggregate data in column 'column_name_2'
# aggregate data by count, mean
# sort values in 'count' column by descending order
# convert data in mean column from float to percent (0.498 -> 49.8%)
# color background of cells in 'mean' column to green where 'mean' value > 30%
(df.groupby(['column_name_1'])
    ['column_name_2']
    .agg(['count', 'mean'])
    .sort_values('count', ascending=False)
    .style
    .format({'mean': '{:,.1%}'.format, })
    .applymap(lambda x: 'background-color : green' if x > 0.3 else '', subset=['mean']))


# PIVOT TABLE
# create pivot table where:
# rows -> index column 'column_name_1'
# columns -> values in 'column_name_2'
# values -> data in columns 'column_name_3' and 'column_name_4'
# aggregate values as 'count' and 'mean'
df.pivot_table(index='column_name_1',
               columns='column_name_2',
               values=['column_name_3', 'column_name_4'],
               aggfunc=['count', 'mean'],
               margins=True)


# BINS
# define 5 groups (bins) by values in 'column_name'
df['column_name_bins'] = pd.cut(df['column_name'], 5)


# define 5 equal groups (bins) by values in 'column_name'
df['column_name_bins'] = pd.qcut(df['column_name'], 5)


# define 5 groups (bins) by values in 'column_name' where bins are:
# 0-1000, 1000-2000, 2000-3000, 4000-5000, 5000-others
df['column_name_bins'] = pd.cut(df['column_name'], [0, 1000, 2000, 3000, 5000, np.inf])


# define 2 groups (bins) by value in 'column_name' where bins are:
# 0-1000, 1000-others
# rename 'bins' in 'column_name_bins' to '0-1k' and '1k+'
df['column_name_bins'] = pd.cut(df['column_name'], [0, 1000, np.inf], labels=['0-1k', '1k+'])


# DUMMIES MATRIX
# converts categorical column to 0-1 matrix where:
# rows -> index column
# columns -> categorical column values
# values 1 - if categorical values is in column index, 0 - if categorical values is not in column index
pd.get_dummies(df['column_name'])
