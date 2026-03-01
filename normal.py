import pandas as pd
import numpy as np
df=pd.read_csv("fds/Housing.csv")
df=df.select_dtypes(include=np.number)
df.head()
max_abs=np.max(np.abs(df),axis=0)
scaled_df=df/max_abs
print(scaled_df.head())
from sklearn.preprocessing import Normalizer
scaler=Normalizer()
scaled_data=scaler.fit_transform(df)
scaled_df=pd.DataFrame(scaled_data,columns=df.columns)
print(scaled_df.head())