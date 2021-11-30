
import sys
input = sys.stdin.readline
n = int(input())
T = []
P = []
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + T[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i]+ dp[i+T[i]], dp[i+1])

print(dp[0])

'''
퇴사
- 문제 설명
제약사항) 상담시 걸리는 시간 
  -> 상담기간 중 다른 상담이 불가
  -> 마지막 날 넘어서는 상담은 불가  

요구사항) 최대 이익

- 문제 풀이 개요

시간복잡도 계산)
1. 3일까지의 최대수익을 활용이 가능하다. => DP
2. N = 1,500,000로 완전탐색 O(N^2)은 불가능하다.

유추 과정)
  1일 2일 3일 4일 5일 6일 7일
T  3   5   1   1   2   4   2
P  10 20  10  20  15  40  200

D : 일차까지 상담시 최대 수익
만약 1일차 상담을 할 경우 vs 안 할 경우
D[1] = 10 + D[4]
vs
D[2]
=> D[i] = max(P[i] + D[i + T[i]], D[i+1])
여기서 재귀는 i + T[i] > n 넘어갈때 끊긴다. 
'''


'''
D[i+1]을 미리 아는 상태에서 풀이가 가능하다. 
미리 알지 않을 경우 재귀함수로 
i = 0
while i < n:
    # 종료 조건
    if i + T[i] > n:
      D[i] = D[i-1]
    else:
      D[i] = max(P[i] + D[i + T[i]], D[i+1])
    i += 1
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
T = []
P = []
D = [0] * (n)
for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
'''
edge case로 틀림

def time_table(x, n):
    global D
    if x >= n:
        return 0

    if x + T[x] > n:
        return D[x-1]

    D[x] = max(P[x] + time_table(x + T[x], n), time_table(x+1, n))
    return D[x]

print(time_table(0, n))
'''
