# 캐릭터가 몇번 움직이는지 
# 캐릭터가 갈곳이 없거나 캐릭터들이 같은곳에 있다가 한명이 이동하는경우
# 일단 어떻게 움직일지에 대한 판단로직을 짜기 어렵다 
# bfs로 하는수밖에 없다. 

# 특정 유저는 이길수밖에 없는 유저 => 최대한 빨리 (단거리)
# 나머지 하나는 질 수 밖에 없는 유저 => 최대한 천천히 지기 (장거리)
# 이길 수 밖에 없는 유저를 어떻게 판단하지?
    # 못하면 다 해봐야겠네 => 1)A로 가정, 2)B로 가정. 짧은 걸로 리턴

# map, 방문해있으면 2, 방문안했다면 1, 이미 방문해서 발판이 없는경우 0
# A,B의 이동 횟수를 따로 체크
# Heap으로 해야하는가? 그렇다면 A, B를 별도 배열로 들고 있어야하는데?
    # A를 먼저 돌고, B를 돌게하면된다. 
def solution(board, aloc, bloc):
    vis = [[0]* m for _ in range(n)]
    block = [[0]* m for _ in range(n)]

    def solve(myx, myy, opx, opy):
        if vis[myx][myy] == 0: return 0
        ret = 0
        for dx, dy in [[-1,0],[0,1],[1.0],[0,-1]]:
            nx = myx + dx
            ny = myy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if vis[nx][ny] or block[nx][ny] == 0: continue
            vis[myx][myy] = 1

            val = solve(opx, opy, nx, ny) + 1
            
            vis[myx][myy] = 0

            # if ret % 2 == 0 and val % 2 == 1: 

    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]

    return answer