##pypy3만 4300ms으로 통과
def bin_search(a, key) -> int:
    pl = 0
    pr = len(a) -1 

    while True:
        pc = (pl + pr)//2 # 중앙원소의 값
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr:
            break
    return 0

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort() # 이진 탐색을 위해선 Sort된 상태여야 효율적이다. 

for i in range(m):
    print(bin_search(A, B[i]))
