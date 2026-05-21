import sys
for line in sys.stdin:
    if line.strip():
        print("lines", 1)


import sys
counts = {}
for line in sys.stdin:
    key, val = line.strip().split()
    counts[key] = counts.get(key, 0) + int(val)
for key, value in counts.items():
    print(key, value)
