import sys

count = [0]*10001
N = int(sys.stdin.readline())

for i in range(N):
    number = int(sys.stdin.readline())
    count[number]+=1
    
for i in range(1,10001):
    if count[i]>0:
        for _ in range(count[i]):
            print(i)