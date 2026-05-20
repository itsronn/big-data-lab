#mapper

#! usr/bin/env python3

import sys
for line in sys.stdin:
    for word in line.strip().split():
        print(word.lower(),1)


#reducer
#! usr/bin/env python3

import sys
counts={}
for line in sys.stdin:
    word,n=line.strip().split()
    counts[word]=counts.get(word,0)+int(n)
for word,counts in counts.items():
    print(word,counts)