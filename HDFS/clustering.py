import sys
centriods=[1,10,20]
for line in sys.stdin:
    for point in line.strip().split():
        p = int(point)
        nearest= min(centriods,key= lambda c: abs(p-c))
        print(nearest,p)

import sys
groups={}
for line in sys.stdin:
    c,p=line.strip().split()
    groups[c]=groups.get(c,[])+[int(p)]
for c,pts in groups.items():
    print(c,sum(pts)/len(pts))

    