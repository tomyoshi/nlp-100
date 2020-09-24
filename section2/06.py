
import pandas as pd


is_input = int(input())

df = pd.read_csv("./testFile/popular-name.txt")
file = pd.read_csv("./testFile/popular-name.txt", chunksize= len(df) // is_input)

for i in file:
    print(i)
