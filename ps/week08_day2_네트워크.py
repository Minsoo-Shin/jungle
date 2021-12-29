from collections import defaultdict

def solution(n, computers):
    answer = 0
    graph = defaultdict(list)

    #dfs
    def dfs(start):
        stack=[start]
        while stack:
            node = stack.pop()
            vis[node] = True
            for next in graph[node]:
                if vis[next] == True: continue
                vis[next] = True
                stack.append(next)
        return 1

    # graph 정보 
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1 :
                graph[i].append(j)
                graph[j].append(i)

    # vis = 2차원
    vis = [[False]*n for _ in range(n)]
    for i in range(n):
        if vis[i] == True: continue
        answer += dfs(i)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] ))
