import pandas as pd

df = pd.read_csv("./testFile/popular-name.txt")

df.sort_values(by='number', ascending=False, inplace=True)

print(df.head())
