import sys
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
n = 2
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,A[i][k]*B[k][j])


import sys
counts={}
for line in sys.stdin:
    word,n=line.strip().split()
    counts[word]=counts.get(word,0)+int(n)
    
for word,counts in counts.items():
    print(word,counts)
