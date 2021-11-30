import bisect
n = int(input())
seq = list(map(int, input().split()))
result = [seq[0]]

for i in range(1, n):
    if seq[i] > result[-1]:
        result.append(seq[i])
    else:
        idx = bisect.bisect_left(result, seq[i])
        result[idx] = seq[i]

print(len(result))

