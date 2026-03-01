import pandas as pd
data={'Id':[101,102,103,104,102,106,101],
      'Name':['Alice','Bob','Charlie','David','Bob','Alice','Alice'],
      'Age':[25,29,29,33,29,27,25],
      'Salary':[55000,48000,55000,62000,48000,59000,55000],
      'City':['NY','LA','NY','SF','LA','LA','NY']}
#orginal dataset
df=pd.DataFrame(data)
print("Original Dataset")
print(df,'\n')
#Exact match-based on all columns
df_cleaned=df.drop_duplicates()
print("Duplicates Removed-Exact Match")
print(df_cleaned,'\n')
#partial match-based on specific columns only('eg.,'ID')
df_cleaned_id=df.drop_duplicates(subset=['Id'])
print("Duplicates removed-partial match based on ID")
print(df_cleaned_id,'\n')
#partial match-based on specific columns only('eg.,'ID')
df_cleaned_name=df.drop_duplicates(subset=['Name'])
print("Duplicates removed-partial match based on Name")
print(df_cleaned_name,'\n')
#partial match-based on specific columns only('eg.,'ID' and 'Name')
df_cleaned_specific=df.drop_duplicates(subset=['Id','Name'])
print("Duplicates removed-partial match based on ID and Name")
print(df_cleaned_specific,'\n')