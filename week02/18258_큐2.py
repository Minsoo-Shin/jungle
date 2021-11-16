import sys
from collections import deque

n = int(input())
deq = deque()

for _ in range(n):
    line = sys.stdin.readline().split()

    if line[0] == 'push':
        deq.append(line[1])

    if line[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            element = deq.popleft()
            print(element)

    if line[0] == 'size':
        print(len(deq))

    if line[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    if line[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else: 
            print(deq[0])

    if line[-1] == 'back':
        if len(deq) == 0:
            print(-1)
        else: 
            print(deq[-1])    

    