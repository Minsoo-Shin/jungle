from itertools import permutations
import sys

n = int(input())
array = [list(map(int, sys.stdin.readline().rstrip().rsplit())) for i in range(n)]
result = 1000000000

for i in permutations(range(n)):
    ssum = 0
    for j in range(n-1):
        if array[i[j]][i[j+1]] != 0 and j < n-2:
            ssum += array[i[j]][i[j+1]]
        elif array[i[j]][i[j+1]] != 0 and j == n-2 and array[i[-1]][i[0]] != 0:
            ssum += array[i[j]][i[j+1]]
            ssum += array[i[-1]][i[0]]
            result = min(result, ssum)
        else:
            break
    
print(result)    