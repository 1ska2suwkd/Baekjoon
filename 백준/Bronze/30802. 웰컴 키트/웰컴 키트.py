import math
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠 묶음 계산
cnt = 0
for i in size:
    cnt += math.ceil(i/T)  # 올림 계산

# 펜 묶음 계산
pen_bundles = N // P  # 최대 묶음 수
pen_remainder = N % P  # 나머지 개수

# 결과 출력
print(cnt)
print(pen_bundles, pen_remainder)
