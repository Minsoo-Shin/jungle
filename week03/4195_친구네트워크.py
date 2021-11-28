import sys
input = sys.stdin.readline


# 조상을 찾는다. 
def getP(a):
    if parent[a] == a:
        return a
    parent[a] = getP(parent[a])
    return parent[a]

# 
def union_(a,b):
    a = getP(a)
    b = getP(b)
    if a!=b:
        parent[a] = b
        ans[b] += ans[a]
        

n = int(input())
for i in range(n):
    f = int(input())
    parent = dict()
    ans = dict()
    for j in range(f):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            ans[a] = 1
        if b not in parent:
            parent[b] = b
            ans[b] = 1

        union_(a, b)
        print(ans[getP(a)])

        



# parent 가 다르면 union을 한다. 
# getparent를 하는 함수를 구현한다. 

# 조상을 key로 한다. 
