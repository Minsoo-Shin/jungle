import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = int(sys.stdin.readline())
    heapq.heappush(heap, a)
    
    last_idx = len(heap)-1
    print(heap)
    if last_idx % 2 == 0: # 짝수 
        print(heap[last_idx//2])
    else:
        print(min(heap[last_idx//2], heap[last_idx//2 + 1]))
    