import pandas as pd
data={'Name':['Alice','Bob','Alice'],
      'Scores':[85,90,85]}
df=pd.DataFrame(data)
df_clean=df.drop_duplicates()
df_long=pd.melt(df_clean,id_vars=['Name'],var_name='Metric',value_name='Value')
print(df_long)