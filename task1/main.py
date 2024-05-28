import math
import json
import sys
# task1

n = int(sys.argv[1])
m = int(sys.argv[2])
iter = 1
lengh = m - 1
path = [str(iter)]

while True:
    if iter == n:
        iter = 0
    iter += 1
    lengh -= 1
    if iter == 1 and lengh == 0:
        break
    if lengh == 0:
        lengh = m - 1
        path.append(str(iter))

print(''.join(path))