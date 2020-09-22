
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
is_one = [1, 5, 6, 7, 8, 9, 15, 16, 19]

res_elements = {}

for i, word in enumerate(string.split(), 1):

    if i in is_one:
        res_elements[i] = word[:1]
    else:
        res_elements[i] = word[:2]

print(res_elements)

