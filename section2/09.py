
import pandas as pd

df = pd.read_csv("./testFile/popular-name.txt", sep='\t', header=None)

print(df.sort_values(2, ascending=False))
