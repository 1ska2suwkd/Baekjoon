max_width, max_length = map(int, input().split())
width_cuts = [0, max_width] 
length_cuts = [0, max_length]

N = int(input())

for i in range(N):
    is_length, number = map(int, input().split())

    # 1
    if is_length:
        width_cuts.append(number)
    # 0
    elif not is_length:
        length_cuts.append(number)

width_cuts.sort()
length_cuts.sort()

print(width_cuts)
print(length_cuts)