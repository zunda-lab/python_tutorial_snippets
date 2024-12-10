import json
x = [1, 'simple', 'list']
json.dumps(x)
# '[1, "simple", "list"]'

f = open('workfile', 'w', encoding="utf-8")

json.dump(x, f)

f.close()

f = open('workfile', encoding="utf-8")

x = json.load(f)

x
# [1, 'simple', 'list']

