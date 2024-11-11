remainders = set() #중복을 허용하지않는 set 사용

for _ in range(10):
    n = int(input())
    remainders.add(n%42) #set이기 때문에 append가 아닌 add 사용

print(len(remainders)) #중복되지 않는 수들의 개수를 출력
