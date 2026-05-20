import sys,hashlib
size=20
for line in sys.stdin:
    for word in line.strip().split():
        print(int(hashlib.md5(word.encode()).hexdigest(),16)%size)
        print(int(hashlib.sha1(word.encode()).hexdigest(),16)%size)


import sys,hashlib
size=20
bits=[0]*size
for line in sys.stdin:
    bits[int(line.strip())]=1

queries=["apple","banana","grape"]
for q in queries:
    h1=int(hashlib.md5(q.encode()).hexdigest(),16)%size
    h2=int(hashlib.sha1(q.encode()).hexdigest(),16)%size
    print(q,"-> EXISTS" if bits[h1] and bits[h2] else "-> DOES NOT EXIST")