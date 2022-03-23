'''
1. 아이디어
    - 시작점을 1번으로 넣고, dfs로 몇개까지 연결되어있는지 확인하면 된다. 
2. 시간 복잡도
    - V 100, E 100C2 = 10000 => 만개

3. 자료구조
    - 그래프
    - 방문이력
    - 스택
'''

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [False] * (n+1)
def dfs(start):
    cnt = 0
    vis[start] = True
    stack = [start]
    while stack:
        node = stack.pop()
        for nex in graph[node]:
            if vis[nex] == False:
                vis[nex] = True
                cnt += 1
                stack.append(nex)
    return cnt

print(dfs(1))