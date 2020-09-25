import json


with open("./testFile/jawiki-country.json", encoding='utf-8') as f:

    for line in f:
        line = json.loads(line)

        if line['title'] == 'イギリス':
            print(line['text'])
