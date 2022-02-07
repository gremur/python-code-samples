import pandas as pd

df = pd.DataFrame()

# clone existing dataframe into new one.
# the code below is equal to 'new_df = df.copy(deep=True)' because 'deep=True' option is default
new_df = df.copy()
