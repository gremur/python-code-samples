import pandas as pd

df = pd.DataFrame()

# convert Unix timestamps like '1387295797' to '2013-12-17 15:56:37'
df['unix_datetime'] = df['unix_datetime'].astype(int)
df['datetime'] = pd.to_datetime(df['unix_datetime'], unit='s')
