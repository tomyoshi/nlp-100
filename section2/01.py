

with open("./testFile/popular-name.txt", "r") as f:
    
    for i, line in enumerate(f, 1):
        print(line.replace("\t", " "), end="")
        if i == 5:
            break
