

import json
import re

pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'

with open("./testFile/jawiki-country.json", "r") as f:

    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text = line['text']

result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text, re.MULTILINE))
print(result)
