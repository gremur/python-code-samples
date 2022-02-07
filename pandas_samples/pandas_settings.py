import pandas as pd

# show all columns in pandas dataframe preview
pd.set_option('display.max_columns', None)

# set the maximum width of columns. Cells of this length or longer will be truncated with an ellipsis
pd.set_option('display.max_colwidth', 100)

# turn off 'SettingWithCopyWarning:  A value is trying to be set on a copy of a slice from a DataFrame'
pd.options.mode.chained_assignment = None
