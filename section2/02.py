

with open("./testFile/popular-name.txt", "r") as f:

    file_col1 = "col1.txt"
    file_col2 = "col2.txt"

    col1_obj = open(file_col1, "w", encoding="utf-8")
    col2_obj = open(file_col2, "w", encoding="utf-8")

    for line in f:
        col1_obj.write(line.split()[0] + "\n")
        col2_obj.write(line.split()[1] + "\n")

    col1_obj.close()
    col2_obj.close()


