'''
평범한 배낭

- 문제 설명
 > N개의 물건. 그 물건 마다의 무게 W와 가치 V가 있다. 
 > 준서는 버틸 수 있는 무게가 정해져 있다. 그 무게에서의 최대 가치를 구한다. 

- 제약 사항) 들 수 있는 무게 K
- 요구 사항) 가치의 최대값 

시간 복잡도)
물품의 수 (<100)라 물품별 모두 비교한다면, 시간 복잡도는 어떻게 될까?

유추과정)
무게 w, 가치 v
물품 
   1  2  3  4  5
w  4  6  4  3  5
v  7 13  8  6 12 

테이블 구성)
D
w 
D[i][j] = max(D[i-1][j], D[i-1][)

'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
pack = [[0,0]]
knapsack = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    w, v = map(int, input().split())
    pack.append([w,v])
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = pack[i][0]
        value = pack[i][1]
        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else: # 물품의 무게가 견딜수 있는 무게보다 가볍다면 고려대상
            knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])

print(knapsack[n][k])