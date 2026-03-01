import pandas as pd
#creating dataset
data = { 'ID':[ 101,102,103,104,105],
        'name': ['vamsi','raju','teja','shannu','sai'],
        'age':[25,None,29,33,None],
        'salary':[55000,48000,None,62000,None]}

df = pd.DataFrame(data)
print(df)
#printing after removing null rows
df_cleaned = df.dropna()
print(df_cleaned)
for column in df.columns:
    if df[column].dtype == 'float64' or df[column].dtype == 'int64':
        df[column].fillna(df[column].mean(), inplace=True)
print(df)
# imputing missing values with mean
for c in df.columns:
  if df[c].dtype == 'float64' or df[c].dtype =='int64':
    df[c].fillna(df[c].mean(),inplace=True)
print(df)
#create a coulumn based flag
for column in df.columns:
  if df[column].isnull().any():
    df[f"{column}_flag"]=df[column].isna().apply(lambda x:'Missing' if x else 'Not Missing')
#create a row based flag
df['Missing_flag']=df.isnull().any(axis=1).apply(lambda x:'Missing' if x else 'Not missing')
print(df)