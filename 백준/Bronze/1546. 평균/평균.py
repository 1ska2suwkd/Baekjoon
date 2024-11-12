n =int(input())
sum = 0

lis = list(map(int,input().split()))
m = max(lis)

for i in lis:
    sum+=i/m*100
avg = sum/n

print(avg)