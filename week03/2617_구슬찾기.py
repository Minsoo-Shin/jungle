import sys
from collections import defaultdict
import heapq
n, m = map(int, sys.stdin.readline().split())
ans = 0
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
parent = list(range(n+1))

def addParentsScore(el, rank):
    while True:
        if parent[el] == el:
            rank[el][0] -= 1
            break
        rank[el][0] -= 1
        el = parent[el]
###################################
rank_a = []
for i in range(n+1):
    rank_a.append([0, i])

for i in arr:
    parent[i[0]] = i[1]
    addParentsScore(i[1], rank_a)
    # a 위에 있는 모든 조상들의 Rank를 1씩 올려주면 된다. 


heapq.heapify(rank_a)
for i in range(len(rank_a)):
    tmp = heapq.heappop(rank_a)
    if -tmp[0] + 1 > (n+1)/2:
        ans += 1
###################################
rank_b = []
for i in range(n+1):
    rank_b.append([0, i])

parent = list(range(n+1))

for i in arr:
    parent[i[1]] = i[0]
    addParentsScore(i[0], rank_b)
    # a 위에 있는 모든 조상들의 Rank를 1씩 올려주면 된다. 

heapq.heapify(rank_b)
for i in range(len(rank_b)):
    tmp = heapq.heappop(rank_b)
    if -tmp[0] + 1 > (n+1)/2:
        ans += 1

print(ans)
