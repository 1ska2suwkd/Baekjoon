h, m = map(int,input().split( ))

M = m - 45
if (M<0):
    h-=1
    M+=60
    if(h<0):
        h+=24
        
print(h, M)