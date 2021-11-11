# BOJ 2468 - 안전 영역
import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, rain):
    need_visited= []
    need_visited.append((x,y))
    while need_visited:
        root = need_visited.pop()
        if visited[root[0]][root[1]] == False:
            visited[root[0]][root[1]] = True
            for i in range(4):
                nx = root[0] + dx[i]
                ny = root[1] + dy[i]
                if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and (heights[nx][ny] > rain):
                    need_visited.append((nx,ny))
                    
                        
n = int(sys.stdin.readline())
heights = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, heights))
min_height = min(map(min, heights))

ans = 1
for rain in range(min_height, max_height):
    visited = [[False]*n for i in range(n)]
    safe = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and heights[r][c] > rain:
                safe += 1
                DFS(r, c, rain)
    ans= max(ans, safe)
print(ans)