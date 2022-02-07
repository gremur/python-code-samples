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
