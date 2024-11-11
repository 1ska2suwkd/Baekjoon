t = int(input())

for _ in range(t):
    cnt = 1
    score = 0
    
    s = input()
    
    for i in s:
        if i == 'O':
            score+=cnt
            cnt+=1
        elif i == 'X':
            cnt = 1

    print(score)