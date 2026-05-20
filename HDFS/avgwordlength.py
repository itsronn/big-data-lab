#mapper 
#! usr/bin/env python3

import sys
for line in sys.stdin:
    for word in line.strip().split():
        print("length",len(word))

#reducer
#! usr/bin/env python3

import sys
val=[]
for line in sys.stdin:
    _,n=line.strip().split()
    val.append(int(n))
print("avg word len", sum(val)/len(val))