import pandas as pd

df = pd.DataFrame()

# find all instances (in all columns and cells) of 'find_item' in dataframe and replace with 'replace_with_item'
# without creation of new dataframe, existing dataframe will be overwritten
df.replace('find_item', 'replace_with_item', inplace=True)

# find all instances (in all columns and cells) of 'find_item' in dataframe and replace with 'replace_with_item'
# with creation of new dataframe, existing dataframe will keep unchanged
df_new = df.replace('find_item', 'replace_with_item')

# find all instances (in all columns and cells) of 'na' values and replace with 'null'
df.fillna('null', inplace=True)

# replace NA values in column 'column_name' with 'no_info'
df['column_name'] = df['column_name'].fillna('no_info')

# replace categorical column values using dict
replace_with = {0: "null", 1: "one", 2: "two", 3: "three"}
df['column_name'] = df['column_name'].map(replace_with)
