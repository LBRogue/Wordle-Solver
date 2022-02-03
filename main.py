import json
import string

data = json.load(open("dictionary.json"))

data2 = []
for x in data:
    if len(x)==5:
        data2.append(x)
print(data2)
