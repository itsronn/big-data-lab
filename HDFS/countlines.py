import sys

for line in sys.stdin:
    if line.strip():
        print("lines", 1)


import sys

count = 0
for line in sys.stdin:
    key, val = line.strip().split()
    count += int(val)

print("Total lines:", count)