N, M = map(int, input().split())
basket = []
for i in range(N):
    basket.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for number in basket:
    print(number, end = " ")