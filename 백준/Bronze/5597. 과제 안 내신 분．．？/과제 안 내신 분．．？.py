students = []
for i in range(0,30):
    i+=1
    students.append(i)
    
for i in range(0,28):
    remove = int(input())
    students.remove(remove)

result = f"{students[0]}\n{students[1]}"

print(result)