import pandas as pd

df = pd.DataFrame()

# show column names
columns = df.columns

# converts column names to list
columns_list = df.columns.values

# rename column in dataframe, existing dataframe will be overwritten
df.rename(columns={'column_name': 'new_column_name'}, inplace=True)

# rename all columns by replacing a part of column name
df.columns = df.columns.str.replace("hashtag_", "ht_")

# rename columns with new columns names in the list
df.columns = ['column_name_1', 'column_name_2', 'column_name_3']

# rename columns. replace chars in column name, convert lo lower case
df.columns = ['column_name_1', 'column_name_2', 'column_name_3']
df.columns = df.columns.str.replace('_', '-').str.lower()

# rename columns in multi column index pivot dataframe
# flat multi index columns
# create new column names by concatenate multi index with '_'
df.columns = ['_'.join(col).strip() for col in df.columns.values]
