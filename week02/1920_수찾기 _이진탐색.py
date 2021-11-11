import math
import time

start = time.time() 

def bin_search(a, key) -> int:
    pl = 0
    pr = len(a) -1 

    while True:
        pc = (pl + pr)//2 # 중앙원소의 값
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            return 0

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(m):
    print(bin_search(A, B[i]))

end = time.time()
print(f"{end - start:.5f} sec")