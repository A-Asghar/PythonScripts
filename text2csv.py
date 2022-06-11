import pandas as pd
#df = pd.read_csv("t2c.csv" , encoding='cp1252')
df = pd.read_csv("849548018942 (1).txt" , delimiter = '\t' ,encoding='cp1252')

#df_filtered = df.drop(df[ (df['reason']) !='M' or (df['reason'] != 'E') ]).index
df_filtered = df.loc[ (df.reason == 'M') | (df.reason == 'E')]

print(df_filtered['reason'])
#print(df.head(n=5))