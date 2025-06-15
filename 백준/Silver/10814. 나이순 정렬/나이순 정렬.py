N = int(input())
information = []

for _ in range(N):
    age,name = input().split()
    information.append((int(age),name))
information.sort(key=lambda x: x[0]) #x는 매개변수 x[0]은 리턴값
        
for member in information:
    print(member[0],member[1])