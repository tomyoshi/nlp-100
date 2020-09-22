
str = "I am an NLPer"

char_bi_gram = []
word_bi_gram = []

for i in range(len(str)-1):
    char_bi_gram.append(str[i:i+2])
    
for i in range(len(str.split())-1):
    split_word = str.split()
    word_bi_gram.append(split_word[i:i+2])

print(char_bi_gram)
print("")
print(word_bi_gram)
