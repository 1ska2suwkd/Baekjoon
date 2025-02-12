def palin(x,y):
    for i in x:
        y.append(i)
    y.reverse()

x = [1]    

while(True):
    y = []
    x = list(input(""))
    if x[0] == '0':
        break
    
    palin(x,y)

    if x == y:
        print("yes")
    else:
        print("no")