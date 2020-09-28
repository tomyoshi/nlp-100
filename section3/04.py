
import json
import re

pattern = r'\[\[ファイル:(.+?)\|'

with open("./testFile/jawiki-country.json", "r") as f:

    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text = line['text']

result = '\n'.join(re.findall(pattern, text))
print(result)
