import sys

class Stack:
    def __init__(self,capacity=10000):
        self.top = -1 #Stack 상단에 있는 인덱스 번호
        self.capacity = capacity
        self.array = [None]*self.capacity

    def isEmpty(self):
        if self.top == -1:
            return 1
        else: return 0
    
    def push(self,e):
        self.top+=1
        self.array[self.top] = e
    
    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.array[self.top] = None
            self.top-=1
            return e
        else: return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: return -1

    def size(self):
        return self.top+1

S = Stack()
N = int(input(""))

for _ in range(N):
    cmd = sys.stdin.readline().strip() #strip을 쓰는 이유는 개행문자 \n을 지우기 위해
    if "push" in cmd:
        l = cmd.split()
        S.push(int(l[-1]))
    elif cmd == "pop": #strip을 사용하지않으면 "pop\n" != "pop"
        print(S.pop())
    elif cmd == "size":
        print(S.size())
    elif cmd == "empty":
        print(S.isEmpty())
    elif cmd == "top":
        print(S.peek())
    else:
        break