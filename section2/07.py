# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd

df = pd.read_csv("./testFile/popular-name.txt")

print(len(df.drop_duplicates(subset='name')))
