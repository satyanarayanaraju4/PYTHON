import pandas as pd
data={
  's.no':[1,2,3,4,5,6,7],
  'roll':[66,479,110,124,243,57,27],
  'name':['RAJU','VAMSI','TEJA','KIRAN','SATISH','CHAKRI',"ARAVIND"],
  'marks':[99,99,50,100,76,78,54],
  'per':[9,None,5,10,7,None,None]
}
df=pd.DataFrame(data)
print(df)
df_cleaned = df.dropna()
print(df_cleaned)
for c in df.columns:
  if df[c].dtype =='float64' or df[c].dtype =='int64':
