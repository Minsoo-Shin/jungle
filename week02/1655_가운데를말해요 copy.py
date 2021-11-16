import heapq
import sys

left_heap = []
right_heap = []

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-a, a))
    else:
        heapq.heappush(right_heap, (a, a))
    
    if right_heap and left_heap[0][1] > right_heap[0][1]:
        left_num = heapq.heappop(left_heap)[1]
        right_num = heapq.heappop(right_heap)[1]
        heapq.heappush(left_heap, (-right_num, right_num))
        heapq.heappush(right_heap, (left_num, left_num))
    print(left_heap[0][1])