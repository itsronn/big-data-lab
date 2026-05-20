import sys

for line in sys.stdin:
    for word in line.strip().split():
        if len(word) > 5:
            print("longword", 1)


import sys

count = 0
for line in sys.stdin:
    key, val = line.strip().split()
    count += int(val)

print("Total long words:", count)