import sys

## 부모 노드를 찾는 함수
def getParent(parent, x :int):
    if parent[x] == x: return x
    return getParent(parent, parent[x])

## 두 부모 노드를 합치는 함수
def unionParent(parent, a, b):
    a= getParent(parent, a)
    b= getParent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

v,e = map(int, sys.stdin.readline().split())
edge = []
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    edge.append([c, a, b])

## 가중치를 오름차순으로 정렬을 한다. => 그리디 알고리즘
edge.sort()

parent = list(range(v+1))
ssum = 0
for w, s, e in edge:
    # 같은 조상을 가지고 있는지
    if getParent(parent, s) != getParent(parent, e):
        unionParent(parent, s, e)
        ssum += w

print(ssum)