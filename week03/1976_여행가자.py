import sys
input = sys.stdin.readline

def getP(a):
    if parents[a] == a:
        return a
    parents[a] = getP(parents[a])
    return parents[a]

def union(a, b):
    a = getP(a)
    b = getP(b)
    if a != b:
        parents[a] = b

n = int(input()) # 도시의 수
m = int(input()) # 여행 계획에 속한 도시의 수
a = [list(map(int, input().split())) for _ in range(n)] # 연결 정보
plan = set(list(map(int, input().split()))) # 여행 계획 
parents = list(range(n+1)) # 부모노드 테이블 (index = 도시번호)
#print(plan)
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] == 1:
            if getP(i+1) !=  getP(j+1):
                union(i+1, j+1)

ans = set([getP(parents[i]) for i in plan]) #i는 1부터N이기 때문에 
if len(ans) == 1:
    print("YES")
else:
    print("NO")


# i는 0, 1, 2로 들어가는데,
# getP(parents[i+1]) 여기에 들어가는 요소가 아니다. 
# ispos = True

# for i in range(len(plan)-1):
#     if getP(parents[i+1]) != getP(parents[i+2]):
#         ispos = False


# if ispos:
#     print('YES')
# else:
#     print('NO')

# ispos = True
# plan = list(plan)
# for i in range(len(plan)-1):
#     if getP(plan[i]) != getP(plan[i+1]):
#         ispos = False

# if ispos:
#     print('YES')
# else:
#     print('NO')

