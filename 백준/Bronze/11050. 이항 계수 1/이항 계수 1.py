def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n-=1
    return result
    
N, K = map(int, input().split())

top = factorial(N)
bottom = factorial(K) * factorial(N-K)

print(top//bottom)