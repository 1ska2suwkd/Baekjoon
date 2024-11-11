A = int(input())
B = int(input())
C = int(input())

res = A*B*C
res_str = str(res)

for i in range(10):
    cnt = res_str.count(str(i))
    print(cnt)