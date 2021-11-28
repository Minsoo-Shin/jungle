k = int(input())
a = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def makeTree(a, x):
    mid = len(a)//2
    tree[x].append(a[mid])
    if len(a) == 1:
        return    
    makeTree(a[:mid], x + 1)
    makeTree(a[mid+1:], x + 1)

makeTree(a, 0)

for i in range(k):
    print(*tree[i])
