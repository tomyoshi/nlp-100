
import re

res = []

def enigma(str):
    for c in str:
        if re.search('[a-z]', c):
            res.append(chr(219 - ord(c)))
        else:
            res.append(c)    

    return res

if __name__ == "__main__":
    print("".join(enigma(input())))

