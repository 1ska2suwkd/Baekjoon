t = int(input())


for _ in range(t):
    cnt=0
    hotel = []
    h,w,n = map(int,input().split())\
        
    #호텔의 크기에 맞는 객실 번호를 매기는 반복문
    for i in range(1,h+1):
        hotel_w = []
        for j in range(1,w+1):
            hotel_w.append(i*100+j)
        hotel.append(hotel_w)
        
    #주어진 규칙에 맞는 n번째 손님 방을 찾는 반복문 
    for i in range(w):
        for j in range(h):
            cnt+=1
            if cnt == n:
                result = hotel[j][i]
                print(result)