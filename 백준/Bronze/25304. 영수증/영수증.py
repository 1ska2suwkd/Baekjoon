price = int(input())
N = int(input())
sum = 0

for i in range(N):
    item, count = map(int, input().split())
    sum += item*count

if price == sum: print("Yes")
else: print("No")