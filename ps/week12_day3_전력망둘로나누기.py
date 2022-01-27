from collections import defaultdict
from multiprocessing.connection import answer_challenge


# 전선마다 하나씩 자르고,
# dfs를 돌면서 몇개가 나왔는지?
# 그러면 차이를 구할 수 있다. min값은 저장하자 answer


from collections import defaultdict
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    def dfs(start, cnt):
        for next in graph[start]:
            if start in cut_wire and next in cut_wire: continue
            if visited[next] == False:
                visited[next] = True
                cnt += 1
                cnt = dfs(next, cnt)
        return cnt
    
    for wire in wires: # wire전선이면 pass
        cut_wire = [wire[0], wire[1]]
        visited = [False] * (n+1)
        visited[1] = True
        cnt = dfs(1,1)
        answer = min(answer, abs((n - cnt) - cnt))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
