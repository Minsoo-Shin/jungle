'''
1. 아이디어
    1-N까지 자연수 중 중복없이 M개를 고른 수열
    모든 경우의수를 찾을때 백트래킹 문제
    for문
    방문여부를 확인하고 (중복허용X)
    결과값에 넣고
    방문여부를 풀고, 결과값 pop
    재귀 
2. 시간복잡도
    N! 8미만
3. 자료구조
    vis : 재방문 금지 bool[]
    rs : 리스트 결과값 int[]
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
rs = []
vis = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1,n+1):
        if vis[i] == False:
            vis[i] = True
            rs.append(i)
            recur(num+1)
            vis[i] = False
            rs.pop()
recur(0)