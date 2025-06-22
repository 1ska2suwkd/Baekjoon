N,K = map(int,input().split())
people = list(range(1,N+1))
index = K-1
result = []

while len(people):
    result.append(people[index])
    del people[index]
    if len(people) != 0:
        index = (index+K-1)%len(people)

print("<"+", ".join(map(str,result))+">")