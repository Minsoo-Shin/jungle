import sys
import collections

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n-1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
print(graph)
visited = []
ans = []
def DFS(graph, root):
    stack = [root] # stack = 가야할 위치를 저장
    while stack: 
        node = stack.pop() 
        if node not in visited: # 방문 이력이 없다면
            visited.append(node) # 방문 이력에 기록을 남기고
            need_to_visit = list(set(graph[node])-set(visited))
            stack.extend(need_to_visit) # 해당 노드와 연결된 노드를 (방문 이력 있는곳을 제외한) stack에 저장
            for nod in need_to_visit: # 
                ans.append([nod, node])
DFS(graph, 1)
ans.sort()
for a in ans:
    print(a[1])
