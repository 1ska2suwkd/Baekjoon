t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    # 층과 방 번호를 계산합니다.
    floor = (n-1) % h + 1
    room_number = (n-1) // h + 1
    result = floor * 100 + room_number
    
    print(result)

#6층인 호텔에 10번째 손님 
