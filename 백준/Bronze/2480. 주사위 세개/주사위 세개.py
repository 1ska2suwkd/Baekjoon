n1,n2,n3 = map(int,input().split())
count = 0
list = [0,0,0,0,0,0,0]

list[n1] += 1
list[n2] += 1
list[n3] += 1

for i in list:
    if i == 3:
        winning = 10000+count*1000
        print(winning)
        exit()
    elif i == 2:
        winning = 1000+count*100
        print(winning)
        exit()
    count+=1

winning = max(n1,n2,n3) * 100
print(winning)