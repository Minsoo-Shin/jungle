nums = []
for _ in range(2):
    nums.append(int(input()))

x, y = nums[0], nums[1]

if x>0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("잘못 입력되었습니다. ")



