n1,n2,n3 = map(int,input().split())
nums = [n1,n2,n3]
s = set(nums)

if len(s) == 1:
    prize = 10000 + n1 * 1000
    print(prize)
elif len(s) == 2:
    for i in nums:
        if nums.count(i) == 2:
            prize = 1000 + i * 100
            print(prize)
            break
else:
    prize = max(nums) * 100
    print(prize)