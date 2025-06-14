ISBN = list(input())
sum=0
for index in range(13):
    if ISBN[index] == '*':
        damaged = index
    else:
        digit = int(ISBN[index])
        if index%2==0:
            sum+=digit
        else:
            sum+=3*digit

for number in range(10):
    if damaged%2 == 0:
        temp_sum = sum+number
    else:
        temp_sum = sum+3*number

    if temp_sum%10 == 0:
        print(number)
        break