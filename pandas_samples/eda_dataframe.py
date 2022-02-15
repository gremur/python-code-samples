import pandas as pd
import seaborn as sns

df = pd.DataFrame()


# count missing values
df.isnull().sum()

# show unique values in column
df['column_name'].unique()

# show chart visualisation of missing data in all dataframe columns
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
