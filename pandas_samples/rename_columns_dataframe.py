import pandas as pd

df = pd.DataFrame()

# rename column in dataframe, existing dataframe will be overwritten
df.rename(columns={'column_name': 'new_column_name'}, inplace=True)

# rename all columns by replacing a part of column name
df.columns = df.columns.str.replace("hashtag_", "ht_")


