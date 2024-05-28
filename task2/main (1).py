import math
import json
import sys

# task 2
path1 = sys.argv[1]
path2 = sys.argv[2]
with open(path1, 'r', encoding='utf-8') as file:
    l = [line.rstrip() for line in file.readlines()]
    xo, yo = [int(i) for i in l[0].split()]
    ro = int(l[1])
with open(path2, 'r', encoding='utf-8') as file1:
    l1 = [line.rstrip() for line in file1.readlines()]
    list_of_coord = list()
    for line in l1:
        xt, yt = [int(i) for i in line.split()]
        list_of_coord.append((xt, yt))
for point in list_of_coord:
    segment_len = math.sqrt((point[0] - xo)**2 + (point[1] - yo)**2)
    if segment_len > ro:
        print(2)
    elif segment_len == ro:
        print(0)
    else:
        print(1)

    


    






