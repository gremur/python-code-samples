from typing import Union
import numpy as np
import pandas as pd
import dask.dataframe as dd


def to_dask(df: Union[pd.DataFrame, dd.DataFrame]) -> dd.DataFrame:
    """Convert a pandas dataframe to a dask dataframe."""
    if isinstance(df, dd.DataFrame):
        return df

    df_size = df.memory_usage(deep=True).sum()
    npartitions = np.ceil(df_size / 128 / 1024 / 1024)  # 128 MB partition size
    return dd.from_pandas(df, npartitions=npartitions)
