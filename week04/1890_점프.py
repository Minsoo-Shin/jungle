# 4<N<100인데, 모든 경우의 수를 찾기 위해선 2^N으로 시간, 메모리 초과

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

q = deque()
q.append( [matrix[0][0], 0,0] )
cnt = 0
while q:
    move, x, y = q.popleft()
    # 경로의 수를 체크하기 위해 따로 방문 처리하지 않음.
    for dx, dy in ((1,0), (0,1)):
        nx, ny = x + move*dx, y + move*dy
        if nx < 0 or ny < 0 or nx >= n or ny >=n: continue
        if nx == n-1 and ny == n-1:
            cnt += 1
            continue
        q.append([matrix[nx][ny], nx, ny])

print(cnt)