list = []
cnt = 10
for i in range(10):
    n = int(input())
    list.append(n%42)
    
    if list.count(n%42) >= 2:
        cnt-=1

print(cnt)