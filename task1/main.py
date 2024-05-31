import math
import json
import sys
# task1

n = sys.argv[1]
m = sys.argv[2]
if n < 1:
    print('numbers from 1 to n means n is greater than 1, so.. enter positive n please')
else:
    if m > 0:
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
    else:
        iter = 1
        lengh = abs(m) - 1
        path = [str(iter)]
        
        while True:
            if iter == 1:
                iter = iter + n
            iter -= 1
            lengh -= 1
            if iter == 1 and lengh == 0:
                break
            if lengh == 0:
                lengh = abs(m) - 1
                path.append(str(iter))
    print(''.join(path))
