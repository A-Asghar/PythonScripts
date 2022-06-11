import pandas as pd

df = pd.read_csv("cars.csv", delimiter=';')
df = df.iloc[1:407]
#print(len(df.index))
#print(df.head(n=50))
print(df.Origin.str.split(expand=True).stack().value_counts())



