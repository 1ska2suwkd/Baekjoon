def cut_paper(max_value, min_value, number):
    if number <= max_value // 2:
        min_value = number
    elif number > max_value // 2:
        max_value = number

    return min_value, max_value
    
# 가로는 0으로 시작 세로는 1로 시작
max_width, max_length = map(int, input().split())
min_width = min_length = 0

N = int(input())

for i in range(N):
    is_length, number = map(int, input().split())

    if not number > max_length and not number > max_width and not number < min_length and not number < min_width:
        if is_length:
            min_width, max_width = cut_paper(max_width, min_width, number)
            print(f"max width = {max_width}, min width = {min_width}")
        elif not is_length:
            min_length, max_length = cut_paper(max_length, min_length, number)
            print(f"max length = {max_length}, min length = {min_length}")

area = (max_length - min_length) * (max_width - min_width)

print(area)