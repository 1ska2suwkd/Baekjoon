T = int(input())

for i in range(T):
    parentheses = input()
    stack = []
    for index in range(len(parentheses)): #입력받은 괄호의 집합을 순회 하는 반복문
        if parentheses[index] == '(':
            stack.append(parentheses[index])
        elif parentheses[index] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append("error")
                break
        
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")