import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
parts = [[0]*(n+1) for _ in range(n+1)]
inDegree = [0] * (n+1)
# graph를 만들어 주고, 진입차수 리스트도 넣어준다. 
for i in range(m):
    a, b, c = map(int, input().split())
    g[b].append((a, c))
    inDegree[a] += 1
# 진입 차수가 0인 노드 번호를 queue에 넣어준다. 
q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
print(q)
print(g)
while q:
    node = q.popleft()
    print(node)
    print(g[node])
    for p, qty in g[node]:
    # 필요한 부품이 있는지 확인 
        if sum(parts[p]) == 0:
            # 없다면 해당 부품이 쓰이는 중간 부품에 필요한 qty를 업데이트해준다. 
            for next in g[p]:
                # 차수를 하나씩 떨어뜨린다.
                print(inDegree)
                inDegree[next] -= 1
                parts[next][p] = qty
                # 진입 차수가 0이 된 노드를 추가해준다.   
        else:
            for next in g[p]:
                for j in parts[p]:
                    inDegree[next] -= 1
                    parts[next][j] += parts[p][j] * qty

        for k in range(1, n+1):
                    if inDegree[k] == 0:
                        q.append(k)

for i in range(1, n+1):
    print(parts[i])