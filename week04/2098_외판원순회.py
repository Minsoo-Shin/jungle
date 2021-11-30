# 각 도시간 이동하는데 드는 비용은 행렬로 주어진다. 
# 각 도시를 순회하는데 드는 최소 여행 경로를 구하는 프로그램을 작성하시오
# 출발지는 0으로 가정한다. 어차피 사이클을 가지는 그래프로 여행 순서에만 영향을 받음
import sys
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF]*(1<<n) for _ in range(n)]

def dfs(cur, visit):
    # 방문 처리가 다 됐으면 출발지로 돌아가는 비용을 리턴
    if visit == (1<<n) - 1:
        if graph[cur][0]:
            return graph[cur][0]
        else:
            return INF
            
    # 이미 최소 비용이 계산 되었다면
    if dp[cur][visit] != INF:
        return dp[cur][visit]
    # 출발지와 연결되어있는 모든 방문 안한 국가를 방문해서 최소 비용을 출력한다. 
    for i in range(1, n):
        if visit & (1 << i) != 0: continue # 방문을 안했다면
        if not graph[cur][i]: continue # 그래프가 있는 경우
        
        dp[cur][visit] = min(dp[cur][visit], dfs(i, visit | 1<<i) + graph[cur][i])
    return dp[cur][visit]

print(dfs(0, 1))