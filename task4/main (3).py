import math
import json
import sys


#task4
path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as file:
    l = [int(line.rstrip()) for line in file.readlines()]
m = sorted(l)[len(l) // 2]
print(sum(abs(v - m) for v in l))

    


    






