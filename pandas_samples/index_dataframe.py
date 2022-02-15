import pandas as pd

df = pd.DataFrame()

# set index column
df.set_index("column_name", inplace=True)

# reset index of dataframe
df = df.reset_index(drop=True)
