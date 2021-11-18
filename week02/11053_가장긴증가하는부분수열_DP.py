import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
result = [1]* n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j]+1)

print(max(result))