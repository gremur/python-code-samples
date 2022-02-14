import pandas as pd

df = pd.DataFrame()

# count qty of 'tokens' separated by space in string
df['column_name'].apply(lambda x: len(x.split(' '))).sum()

# count items in column cells depends of item type
df['new_column_name'] = df['column_name'].str.len()

# count unique items in column
df['new_column_name'].nunique()

# count null value items in column
df['new_column_name'].isnull().sum()

# count frequencies of values in 'new_column_name' column and sort results in descending order
df['new_column_name'].value_counts(sort=True)

# show percentages instead of counts
df['new_column_name'].value_counts(sort=False, normalize=True)
