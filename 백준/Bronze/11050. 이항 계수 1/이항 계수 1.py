N, K = map(int, input().split())

num = N - K 

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n-=1
    return result

N = factorial(N)
K = factorial(K)
num = factorial(num)

print(N//(K*num))