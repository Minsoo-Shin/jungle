import sys
import heapq

commute = []
n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    commute.append((x,y))
commute = sorted(commute, key=lambda x: x[1])
# location마다의 거리가 좁은건 제외
d = int(sys.stdin.readline())
ans = 0
possible = []
for location in commute:
    if location[1] - d > location[0]:
        continue
    else:
        heapq.heappush(possible, location)
        # 가능한건 최소힙에 저장한다.
    while possible[0][0] < location[1] - d:
        heapq.heappop(possible)
        # 옮길때마다 삭제해야하는건 삭제한다. 
    ans = max(ans, len(possible))
# len(possible)최대가 될때마다 갱신한다. 

print(ans)