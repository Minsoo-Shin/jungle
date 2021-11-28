import sys 
from collections import deque

def coin_combination(coins, k):
    q = deque([(1, coin) for coin in coins]) # (갯수, 돈 단위)
    min_num = float('inf')
    part_sum_set = set([coin for coin in coins]) #(묶음 단위) 조합
    while q:
        num, part_sum = q.popleft()
        if part_sum == k: ##part_sum이 원하는 값이라면 최소값인지 확인
            min_num = min(min_num, num)
        for coin in coins: 
            curr_sum = part_sum + coin # Part_sum에 값 추가한다. 
            if curr_sum >  k: # 더한 값이 k보다 넘을 경우 패스
                continue
            if curr_sum not in part_sum_set: # 현재 합이 set에 없다면 추가.
                part_sum_set.add(curr_sum) # 
                q.append((num + 1, curr_sum)) #q에도 동전의 갯수와 함께 추가
    if min_num == float('inf'):
        return -1 
    return min_num

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = sorted([int(input()) for _ in range(n)], reverse=True)
    print(coin_combination(coins, k))