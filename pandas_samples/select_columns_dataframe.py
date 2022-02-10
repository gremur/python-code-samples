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
