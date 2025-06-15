N = int(input())
fact = 1
cnt=0

for i in range(1,N+1):
    fact*=i
strfact = str(fact)

for number in reversed(strfact):
    if number == '0':
        cnt+=1
    else:
        break

print(cnt)