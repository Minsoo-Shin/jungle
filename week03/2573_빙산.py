import sys
import copy
n, m = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열
year = 0

def DFS(r,c):
    global visited, ice_this_year
    stack = [(r,c)]
    while stack:
        x,y = stack.pop()
        if ice[x][y] != 0 and visited[x][y] == 0 and 1<= x <= n-2 and 1<= y <= m-2: # 방문 이력이 없다면 실행
            visited[x][y] = 1
            zero_cnt = 0
            for i in range(4):
                if ice[x + dx[i]][y + dy[i]] == 0:
                    zero_cnt += 1
            if ice[x][y] - zero_cnt <= 0:
                ice_this_year[x][y] = 0
            else:
                ice_this_year[x][y] = ice[x][y] - zero_cnt # 전년도 정보로 주위 0의 갯수만큼 뺀다.
            tmp_list = [(x-1,y), (x,y+1), (x+1,y), (x,y-1)]
            for e in tmp_list:
                if ice[e[0]][e[1]] != 0 and visited[e[0]][e[1]] == 0: # 빙산의 높이가 0이 아니고 방문한 이력이 없다면
                    stack.append((e[0],e[1])) # 다음 방문지 추가

grp_cnt = 0
break_point = False
while True:
    year += 1
    visited = [[0]*m for _ in range(n)] 
    ice_this_year = [[0]*m for _ in range(n)]
    for i in range(1, n-1):  # 1 ~ n-1까지 탐색 (행)
        for j in range(1, m-1): # 1 ~ m-1까지 탐색 (열)
            init = copy.deepcopy(visited)
            DFS(i,j)
            if init != visited: # visited가 달라진다면 새로운 그룹 추가
                grp_cnt += 1
                if grp_cnt >= 2: #출력
                    print(year)
                    break_point = True
                    break
    ice = copy.deepcopy(ice_this_year)
    check_sum = 0
    for i in range(n):
        check_sum += sum(ice[i])
    if check_sum == 0:
        print(0)
        break_point = True
        break
  
