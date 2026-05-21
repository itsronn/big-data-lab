import sys
for line in sys.stdin:
    for word in line.strip().split():
        if len(word) > 5:
            print("longword", 1)


import sys
counts = {}
for line in sys.stdin:
    key, val = line.strip().split()
    counts[key] = counts.get(key, 0) + int(val)
for key, value in counts.items():
    print(key, value)
