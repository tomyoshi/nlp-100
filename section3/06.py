
import json
import re

pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'

with open("./testFile/jawiki-country.json", "r") as f:

    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text = line['text']

template = re.findall(pattern, text, re.MULTILINE + re.DOTALL)

pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'

result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

def remove_markup(text):
  pattern = r'\'{2,5}'
  text = re.sub(pattern, '', text)

  return text

result_rm = {k: remove_markup(v) for k, v in result.items()}
for k, v in result_rm.items():
    print(k + ': ' + v)