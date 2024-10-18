a = []
n = int(input())
for i in range(n):
    num = int(input())
    if num in a:
        continue
    else:
        a.append(num)
        
a.sort()
        
        
print(a)
