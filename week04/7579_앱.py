'''
앱

입력값)
- N, M = N: 앱의 갯수, M: 비워야하는 최소 메모리 (1<=N<=100), (1<=M<=10,000,000)
- unit = 앱들의 메모리 단위 (30,10,20,35,40)
- cos = 비활성화하면서 드는 비용 (3,0,3,5,4)
- D = M 바이트를 확보하는데 드는 최소비용
문제 설명)
- 제약사항 : 
    1) unit들의 합이 M이 넘어야한다.
- 요구사항 :
    1) 비활성화 비용 최소화
'''

'''
# 시간 초과/
n, m = map(int, input().split())
units = [0] + list(map(int, input().split()))
cos = [0] + list(map(int, input().split()))
INF = float('inf')
D = [[INF] * (m+1)]
D[0][0] = 0
for i in range(1, n+1):
    D.append([INF]*(m+1))
    D[i][0] = 0
    for j in range(1, m+1):
        if units[i] > j: #하나의 앱 메모리가 M보다 크다면
            D[i][j] = min(D[i-1][j], cos[i])
        else: # 하나의 앱이 메모리가 M보다 작다면, 추가로 들어갈 여지가 있다.
            D[i][j] = min(D[i-1][j], D[i-1][j-units[i]] + cos[i])

print(D[n][m])
'''

# unit마다 특정 cost로 만들어 낼 수 있는 메모리 최대 여유 공간?
# 앱당 비용(cos)가 cost제한 (D의 열)을 넘어가기 이전까지는 이전껄 받는다. 

# for cost 제한:
#     if cost < Dp의 cost 제한:
#         이전꺼 받고
#     else:
#         이전거 vs 해당 메모리 + Dp(Cost제한 - 메모리)
# if dp >= m:
#     ans.append(cost제한값)

# print(min(ans))

# 통과 코드
INF = float('inf')
n, m = map(int, input().split())
unit = [0] + list(map(int, input().split()))
cos = [0] + list(map(int, input().split()))
D = [[0] * (sum(cos)+1) for _ in range(n+1)]
ans = INF

for i in range(1, n+1):
    for j in range(1, sum(cos)+1):
        if cos[i] > j:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], unit[i] + D[i-1][j-cos[i]])
        if D[i][j] >= m:
            ans = min(ans, j)

print(ans)