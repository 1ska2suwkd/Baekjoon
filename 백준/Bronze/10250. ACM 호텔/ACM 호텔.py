t = int(input())


for _ in range(t):
    cnt=0
    hotel = []
    h,w,n = map(int,input().split())
    for i in range(1,h+1):
        hotel_w = []
        for j in range(1,w+1):
            hotel_w.append(i*100+j)
        hotel.append(hotel_w)
    for i in range(w):
        for j in range(h):
            cnt+=1
            if cnt == n:
                result = hotel[j][i]
                print(result)
