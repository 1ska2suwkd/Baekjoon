N, M = map(int,input().split())
number = list(map(int,input().split()))
max_total = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            total = number[i]+number[j]+number[k]
            if total <= M:
                max_total = max(max_total,total)
print(max_total)