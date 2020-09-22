

str = "paraparaparadise"
str2 = "paragraph"


char_str = []
char_str2 = []

for i in range(len(str) - 1):
    char_str.append(str[i:i+2])

for j in range(len(str2) - 1):
    char_str2.append(str2[j:j+2])

set_s = set(char_str)
set_s2 = set(char_str2)

print("和集合", set_s | set_s2)
print("積集合", set_s & set_s2)
print("差集合", set_s - set_s2)
print("search -> se", "se" in set_s & set_s2)

