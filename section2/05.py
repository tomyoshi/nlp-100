
import pandas as pd


df = pd.read_csv("./testFile/popular-name.txt")

def output_head(N):
  print(df.tail(N))

output_head(int(input()))

