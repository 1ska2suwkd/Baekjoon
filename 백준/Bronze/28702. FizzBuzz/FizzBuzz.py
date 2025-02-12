inputs = []
for _ in range(3):
    inputs.append(input())
    
for i in range(3):
    if inputs[i].isdigit():
        start = int(inputs[i]) - i  # 현재 위치에 맞게 보정
        break
    
def check_fizzbuzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
    
    
print(check_fizzbuzz(start+3))