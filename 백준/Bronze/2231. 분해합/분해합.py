N = int(input())
res=0

for i in range(N):
   lis = list(map(int,str(i)))
   i_sum = sum(lis)
   if N == i_sum + i:
       res = i
       break
   
print(res)