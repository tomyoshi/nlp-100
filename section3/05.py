
import json
import re

pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'

with open("./testFile/jawiki-country.json", "r") as f:

    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text = line['text']

template = re.findall(pattern, text, re.MULTILINE + re.DOTALL)
print(template)

pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'

result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
for k, v in result.items():
  print(k + ': ' + v)
  