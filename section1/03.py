string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi = []

for word in string.split():
    pi.append(len(word.replace(",", "").replace(".", "")))

print(pi)


