inputs = []
for _ in range(3):
    inputs.append(input())
    
for i in range(3):
    if inputs[i].isdigit():
        break
    
if i == 0:
    output = int(inputs[i])+3
if i == 1:
    output = int(inputs[i])+2
if i == 2:
    output = int(inputs[i])+1
    
def check_fizzbuzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
    
    
print(check_fizzbuzz(output))