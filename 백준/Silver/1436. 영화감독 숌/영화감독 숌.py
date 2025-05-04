N = int(input())

num = 666
cnt = 1

while True:
    
    if N == cnt:
        print(num)
        break

    num+=1
    
    if "666" in str(num):
        cnt+=1
        