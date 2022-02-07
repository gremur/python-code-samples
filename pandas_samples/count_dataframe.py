import pandas as pd

df = pd.DataFrame()

# count qty of 'tokens' separated by space in string
df['column_name'].apply(lambda x: len(x.split(' '))).sum()

# count items in column cells depends of item type
df['new_column_name'] = df['column_name'].str.len()


