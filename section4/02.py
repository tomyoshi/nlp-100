
filename = './testFile/neko.txt.mecab'

pop = []
dicts = []
res = set()

with open(filename, mode='r') as f:
    for line in f:

        if line != 'EOS\n':
            line = line.split('\t')

            if len(line) != 2 or line[0] == '':
                continue
            else:
                content = line[1].split(',')
                dict = {'surface': line[0] ,'base':content[6] , 'pos':content[0] , 'pos1':content[1] }
                dicts.append(dict)                
        else:
            pop.append(dicts)
            dicts = []

for p in pop:
  for morph in p:
    if morph['pos'] == '動詞':
      res.add(morph['base'])

for value in list(res)[:9]:
  print(value)

