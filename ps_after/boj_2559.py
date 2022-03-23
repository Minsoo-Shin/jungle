'''
1. 아이디어
    첫 k개의 합을 구한다음 
    for문을 돌면서 앞의 숫자는 더하고 뒤에 숫자는 뺴면서 
    최대값을 갱신해나간다. 

2. 시간 복잡도
    N : 10만
3. 자료구조
    maxv : int 

'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum_nums = sum(arr[:k])
maxv = -float('inf')
for i in range(k, n):
    sum_nums = sum_nums - arr[i-k] + arr[i]
    maxv = max(maxv, sum_nums)
print(maxv)