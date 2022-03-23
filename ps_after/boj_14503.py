'''
1. 아이디어
    while 1:
        청소 횟수 증가
        청소 했음 표시
        for문을 돌면서 
            옆에 청소가 안되어있는게 있다면 그 곳으로 간다
        4군데를 다 봤는데 모두 , 또 벽이라면 뒤로 1칸 간다
        하지만
2. 시간 복잡도

3. 자료구조
    map 0이 빈칸 1 벽 2 방문했음
    cnt 청소한 횟수
    sw 네 방향 다 둘러봤을 때 ...

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [ list(map(int, input().split())) for _ in range(n)]

cnt =0 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while 1:
    if map[x][y] == 0:
        cnt += 1
        map[x][y] = 2
    sw = True
    for i in range(1,5):
        nx, ny = x + dx[d-i], y + dy[d-i]
        if 0<= nx < n and  0<= ny < m:
            if map[nx][ny] == 0: 
                x = nx
                y = ny
                d = (d-i+4)%4
                sw = False
                break

    if sw == True:
        nx, ny = x - dx[d-i], y - dy[d-i]
        if 0 <= nx < n and 0 <= ny <m:
            if map[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
        else:
            break

print(cnt)