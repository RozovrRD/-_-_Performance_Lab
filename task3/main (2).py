import math
import json
import sys

#task3

path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]
with open(path1, "r", encoding='utf-8') as file1:
    info1 = file1.read()
with open(path2, "r", encoding='utf-8') as file2:
    info2 = file2.read()

values = json.loads(info1)
tests = json.loads(info2)

for item in tests['tests']:
    item_id = item['id']
    for val in values['values']:
        if val['id'] == item_id:
            item['value'] = val['value']
            break
with open(path3, 'w', encoding='utf-8') as file3:
    json.dump(tests, file3)


    


    






