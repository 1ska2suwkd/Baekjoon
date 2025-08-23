hour, minute = map(int,input().split())
m = int(input())

minute += m
hour += minute//60
minute %= 60
hour %= 24

print(hour, minute)