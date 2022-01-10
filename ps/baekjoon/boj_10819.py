from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

seq = list(permutations(arr))

max_num = 0
for s in seq:
    ssum = 0
    for i in range(len(s)-1):
            ssum += abs(s[i] - s[i+1])
    max_num = max(max_num, ssum)


print(max_num)
