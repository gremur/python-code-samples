import pandas as pd

df = pd.DataFrame()


# drop columns by column index
df = df.drop(df.columns[[0, 3, 6, 8, 11, 12, 13]], axis=1)

# drop column by name
df.drop('column_name_1', axis=1, inplace=True)
df.drop(['column_name_1', 'column_name_2', 'column_name_3'], axis=1, inplace=True)

# drop rows contain NA, axis=0 means rows, axis=1 means columns
df = df.dropna(axis=0, how="any")

# delete column
del df['column_name']
