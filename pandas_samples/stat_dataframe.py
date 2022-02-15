import pandas as pd

df = pd.DataFrame()

# show unique values in column
df['column_name'].unique()

# create correlation matrix between two columns
df[['column_name_1', 'column_name_2']].corr()
