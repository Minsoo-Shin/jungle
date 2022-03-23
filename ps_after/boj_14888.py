'''
1. 아이디어
    if opCnt의 합이 0이라면
        maxv = max(maxv, rs)
        minv = min(minv, rs)
    
    for i in range(n):
        opCnt[0] != 0라면,
            이제까지의 결과값에 더하거나/뺴거나/곱하기/나누기 (나누기는 별도과정)
            result값에 저장
        opCnt[1] != 0


2. 시간복잡도
    n!

3. 자료구조
    rs : 결과값 저장
    maxv, minv : 전역변수 int
    opCnt : int[ , , , ]
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
opCnt = list(map(int, input().split()))

maxv = -float('inf')
minv = float('inf')

def dfs(depth, total, plus, minus, multiply, divide):
    global maxv, minv
    if depth == n:
        maxv = max(maxv, total)
        minv = min(minv, total)
        return

    if plus:
        dfs(depth + 1, total + arr[depth], plus -1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - arr[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * arr[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total / arr[depth]), plus, minus, multiply, divide-1)

dfs(1, arr[0], opCnt[0], opCnt[1], opCnt[2], opCnt[3])
print(maxv)
print(minv)