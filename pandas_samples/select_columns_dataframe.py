import pandas as pd

df = pd.DataFrame()

# select multiple columns from a dataframe
selected_columns1 = df[['column_name_1', 'column_name_2', 'column_name_3']]

# use lists to select multiple columns
columns_list = ['column_name_1', 'column_name_2', 'column_name_3']
selected_columns2 = df[columns_list]

# select multiple columns using the filter operator
selected_columns3 = df.filter(like="_name_")

# select multiple columns with 'column_name_1' data type
selected_columns4 = df.select_dtypes(include=["column_name_1"])

# exclude the last 3 columns
selected_columns5 = df.iloc[:, :-3]

# select 0 to 7 columns by index
# : means all rows, 0:7 means from 0 to 7 columns
selected_columns6 = df.iloc[:, 0:7]

# select 'item_1', 'item_2', 'item_3' in column 'column_name_1' and show columns 'column_name_1', 'column_name_2' only
selected_columns7 = df.loc[df['column_name_1'].isin(['item_1', 'item_2', 'item_3']), ['column_name_1', 'column_name_2']]
