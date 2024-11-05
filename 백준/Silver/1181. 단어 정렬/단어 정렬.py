n = int(input())
temp = []
res = []

for i in range(n):
    str = input()
    if str in temp:
        temp.remove(str)
    temp.append(str)

temp.sort()

for j in range(50):
    j+=1
    for i in temp: 
        if len(i) == j:
            res.append(i)
            
for i in res:
    print(i)