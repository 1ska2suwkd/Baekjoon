def nextfloor(last_aptnumber,floor):
    next_floor = []
    next_floor.append(last_aptnumber)
    for i in range(n-1,0,-1):
        last_aptnumber -= floor[i]
        next_floor.append(last_aptnumber)
    next_floor.reverse()
    return next_floor

T = int(input())

for _ in range(T):
    K = 0
    floor = []
    k = int(input())
    n = int(input())
    for i in range(n):
        floor.append(i+1)
    while True:
        if K == k:
            print(last_aptnumber)
            break
        last_aptnumber = sum(floor)
        floor = nextfloor(last_aptnumber,floor)
        K+=1