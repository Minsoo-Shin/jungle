# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())

# val = dict()
# for i in range(n):
#     w, v = map(int, input().split())
#     val[w] = v

# items = sorted(val.keys())
# dp = [0] * (k+1)

# for item in items:
#     for j in range(item, k+1):
#         dp[j] = max(dp[j], dp[j-item] + val[item])
       
# print(dp[k])

import sys

N, K = map(int, input().split())
stuff = [[0,0]] # weight/value 값을 왜 2D array로 구성했을까?
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # knapsack도 2D array로 구성했다. (행: 물품, 열: 무게 중량)

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1): # 물품별로 / index를 일대일 매칭
    for j in range(1, K + 1): # 중량 기준/ 
        weight = stuff[i][0]
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] # 물품의 weight가 기준보다 크면 유지
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j]) # 현재 물품과 이전에 들어왔었던 물품 중 여분의 무게 정도의 물품 가치를 합한 값 vs 기존 물품과 비교

print(knapsack[N][K])