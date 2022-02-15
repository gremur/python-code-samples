import pandas as pd

df = pd.DataFrame()

# filter dataframe by exact column value (!= - means not, == - means equal)
df = df[df['column_name'] == 'ru']

# filter dataframe by non-empty cells in column (!= - means not, == - means equal)
df = df[df['column_name'] != '']

# filter dataframe if column cells contain 'http' or 'www' substring
df = df[df['column_name'].fillna('').str.contains("http|www")]

# filter dataframe column values by regex
df = df[df['column_name'].fillna('').str.contains('[a-zа-яё]\\.[A-ZА-ЯЁ]', regex=True, na=False)]

# filter dataframe by items in the another list to be excluded
exclude_items = ['item1', 'item2']
df = df[~df['column_name'].isin(exclude_items)]

# filter dataframe by items in the another list to be kept
keep_items = ['item1', 'item2']
df = df[df['column_name'].isin(keep_items)]

# filter dataframe numerical column by value
df = df[df['column_name'] > 3]

# filter dataframe column by values starts with 'G'
df = df[df['column_name'].str.startswith('G')]

# filter dataframe rows by two columns values, | means OR
df = df[(df["column_name_1"] > 500) | (df["column_name_2"] < 50)]
