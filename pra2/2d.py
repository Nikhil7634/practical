import pandas as pd
df = pd.read_csv('data.csv')
print(df)
df.head(10)
print("Dataset after dropping NA values: ")
df.dropna(inplace = True)
print(df)
