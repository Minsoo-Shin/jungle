import bisect

n = int(input())
nums = list(map(int, input().split()))

nums_2 = list(set(nums[:]))
nums_2.sort()

answer = []
for num in nums:
    answer.append(bisect.bisect_left(nums_2, num))

print(*answer)