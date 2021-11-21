import sys

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 시계방향순
# 빙산을 탐색한 갯수를 찾는 함수
def check(r,c):
    global cnt
    cnt = 1
    stack = [(r,c)]

    visited = [[False] * m for i in range(n)]
    visited[r][c] = True
    while stack:
        r, c = stack.pop()

        for i in range(4):
            nx = r + direction[i][0]
            ny = c + direction[i][1]
            if arr[nx][ny] != 0 and not visited[nx][ny]: # 주변 탐색시 0이 아니고:
                stack.append((nx, ny))
                visited[nx][ny] = True # 방문 표시하고
                cnt += 1
    return cnt
# 탐색한 갯수와 빙산의 정보의 갯수와 같다고 하면 빙산은 하나다.
    # 연도를 올리고, 주변 0의 갯수를 카운팅하여 반영해준다.
# 만약 탐색한 갯수가 빙산의 정보와 다르다고 하면 빙산이 두개임을 의미한다. 

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
melt = [[0] * m for _ in range(n)]
# ice: 빙산이 남아있는 위치를 넣어준다. 
ice = []
for i in range(1, n-1):
    for j in range(1, m-1):
        if arr[i][j] != 0:
            ice.append((i, j))
ans = 0
cnt = 0
year = 0 

while ice:
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = year
        break

    year += 1
    melt_co = []
    for i in range(len(ice) -1, -1, -1):
        x, y = ice[i]

        for dir in range(4):
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]

            if arr[nx][ny] == 0:
                melt[x][y] += 1 
        
        if melt[x][y] > 0:
            melt_co.append((x, y, i))

    for x, y, i in melt_co:
        arr[x][y] -= melt[x][y]
        if arr[x][y] <= 0:
            arr[x][y] = 0
            ice.pop(i)

        melt[x][y] = 0

print(ans)