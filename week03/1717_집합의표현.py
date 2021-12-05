import sys
sys.setrecursionlimit(100000000)

def getParents(a):
    # 종료 조건
    if parents[a] == a:
        return a
    parents[a] = getParents(parents[a]) #경로 최적화
    return parents[a]

def union(a, b):
    a = getParents(a)
    b = getParents(b)
    if a == b: return
    if a < b: parents[b] = a
    else: parents[a] = b

def findUnion(a, b):
    if getParents(a) == getParents(b):
        print("YES")
    else:
        print("NO")

n, m = map(int, sys.stdin.readline().split())
parents = list(range(n+1)) # 노드 갯수의 +1로, Node 0~1~7
for _ in range(m):
    q, a, b = map(int, sys.stdin.readline().split())
    if q == 0:
        union(a, b)
    else:
        # 같은 부모인지 확인해서 출력
        if getParents(a) == getParents(b):
            print("YES")
        else:
            print("NO")