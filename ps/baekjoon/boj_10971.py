# 도시 국가가 N개가 있다. 
# 이동 경로를 순열을 통해서 구하면 될거같다. 이는 한번 갔던 곳을 다시 못갈 뿐더러 
# 도시의 수가 10 미만이다. 
# 경비의 최소값을 구해보자

from itertools import permutations
import sys
INF = sys.maxsize

n = int(input()) # 4
arr = [list(map(int, input().split())) for _ in range(n)]
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0

# 도시의 명은 0~n-1까지다.
min_sum = INF
for test in permutations(range(n)):
    jump = False 
    ssum = 0
    for i in range(n):
        src,
        if i == n-1:
            src, des = test[-1], test[0]
        else:
            src, des = test[i], test[i+1]

        if arr[src][des] == 0: 
            jump = True
            break
        ssum += arr[src][des]

    if jump == True: continue
    min_sum= min(min_sum, ssum)
print(min_sum)

# 10 9, 6, 10
