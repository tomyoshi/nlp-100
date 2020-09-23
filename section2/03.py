import pandas as pd


col1 = pd.read_table("./col1.txt")
col2 = pd.read_table("./col2.txt")


merge = pd.concat([col1, col2], axis=1)

merge.to_csv("merge.txt", sep="\t", index=False)


# 参考
# https://note.nkmk.me/python-pandas-read-csv-tsv/
# https://note.nkmk.me/python-pandas-concat/
