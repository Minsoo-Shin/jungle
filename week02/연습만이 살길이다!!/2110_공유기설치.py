# 가장 인접한 두 공유기의 거리를 기준으로 이분탐색을 해보자
import sys

home, route = map(int, sys.stdin.readline().split())
pos = [int(sys.stdin.readline()) for _ in range(home)]
pos.sort()

start = 0
end = pos[-1] - pos[0]
result = 0

while start <= end:
    mid = (start + end)//2
    loc = pos[0]
    count = 1 # 초기값 
    for i in range(1, home): 
        if pos[i] - loc >= mid:
            count += 1
            loc = pos[i]
        else:
            continue
    if count >= route: # 최소 근접거리 mid로 공유기 설치가 가능하다면
        start = mid + 1 # mid를 늘려본다. 
        result = max(result, mid) # 정답에 근접하는 값들이 max값이면 반영한다. 
    else:
        end = mid - 1

print(result)

