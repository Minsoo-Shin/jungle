# 그래프로를 두개 만든다 위로 정렬 아래로 정렬
# dfs를 리스트 두개로 돌려 원소마다 정리한다음
# 갯수가 n인 원소만 count 해준다. 

from collections import defaultdict

def solution(n, results):
    answer = 0
    up = defaultdict(list)
    down = defaultdict(list)
    cnt_table = [0] * (n + 1)
    
    for result in results:
        a, b = result
        up[b].append(a)
        down[a].append(b)

    def dfs(start, graph):
        cnt = 0
        stack = [start]
        visited = [False]* (n+1)
        while stack:
            cur = stack.pop()
            visited[cur] = True
            for next in graph[cur]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                    cnt += 1
        return cnt

    for start in range(1, n+1):
        if dfs(start, up) + dfs(start, down) == n-1:
            answer += 1
        
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))