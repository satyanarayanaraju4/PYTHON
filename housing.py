import pandas as pd
import numpy as np
df=pd.read_csv("fds/Housing.csv")
df=df.select_dtypes(include=np.number)
df.head()
max_abs=np.max(np.abs(df),axis=0)
scaled_df=df/max_abs
print(scaled_df.head())
