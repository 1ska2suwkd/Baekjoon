import sys

count = [0]*2000001
N = int(sys.stdin.readline())

for _ in range(N):
    number = int(sys.stdin.readline())
    if number<0:
        number = -number+1000000
    count[number]=1
    
for i in range(2000000, 1000000, -1):
    if count[i]>0:
        print(-(i-1000000))
for i in range(0,1000001):
    if count[i]>0:
        print(i)