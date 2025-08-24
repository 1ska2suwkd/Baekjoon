# N은 바구니 수 , M은 공을 넣는 횟수
# i부터 j까지의 바구니에 k번 공을 넣는다.

N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i,j+1):
        basket[index-1] = k

for number in basket:
    print(number, end=" ")