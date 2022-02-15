import pandas as pd

df = pd.DataFrame()


# create correlation matrix between two columns
df[['column_name_1', 'column_name_2']].corr()
