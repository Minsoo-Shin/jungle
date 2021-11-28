# 동전 종류 N, 각 동전은 무한
# 동전 가치의 합을 K로 만든다. 이 때 필요한 동전의 개수를 구하는 프로그램
# N:동전의 종류, K: 동전의 합
# 단위가 있는 동전의 갯수를 적절히 조합해 k원을 만드는 최소갯수를 구해라

import sys
input = sys.stdin.readline
#10종류, 4200원
n, k = map(int, input().split())
#1, 5, 10, 50, 100, 500, 1000 ..
#문제의 조건 (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
coin_unit = [int(input()) for _ in range(n)]
ans = 0

# 동전의 큰 단위로 지불하면 동전의 개수는 최소가 된다. => 그리디 알고리즘
for i in range(n-1, -1, -1):
    if coin_unit[i] <= k:
        ans += k // coin_unit[i]
        k %= coin_unit[i]
        if k == 0: break

# 동전의 개수 최소값은?
print(ans)
