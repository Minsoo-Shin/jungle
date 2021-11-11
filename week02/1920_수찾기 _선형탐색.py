import math
import time

start = time.time() 

def seq_search(a, key):
    i = 0
    while True:
        if i == len(a):
            return 0
        if a[i] == key:
            return 1
        i += 1

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(m):
    print(seq_search(A, B[i]))

end = time.time()
print(f"{end - start:.5f} sec")