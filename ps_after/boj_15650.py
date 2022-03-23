'''
1. 아이디어
    모든 경우의 수를 다 체크하는 것 => 백트래킹
    종료조건 
        num == M
    for문을 돌면서 
        방문 안했으면서 rs의 마지막 원소보다는 큰 원소일 경우에만 통과
        방문 체크
        rs추가
        재귀
        rs삭제
        방문체크 풀고

2. 시간 복잡도
    중복없는 순열이기때문에 N * (N-1) *,,,*(N-M+1)
    N!
3. 자료구조
    vis : bool[]
    rs : int[]
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
vis = [False]*(n+1)
rs = [0]
def recur(num):
    if num == m:
        print(' '.join(map(str, rs[1:])))
    for i in range(1, n+1):
        if vis[i] == False and i > rs[-1]:
            vis[i] = True
            rs.append(i)
            recur(num+1)
            rs.pop()
            vis[i] = False

recur(0)