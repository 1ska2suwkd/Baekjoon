#지피티 코드
N = int(input())
layer = 1
range_end = 1

while N > range_end:
    range_end += 6 * layer
    layer += 1

print(layer)