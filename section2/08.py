import pandas as pd

df = pd.read_csv("./testFile/popular-name.txt", sep="\t", header=None)

df.sort_values(2, ascending=False, inplace=True)

print(df.head())
