from heapq import heappop, heappush
import bisect
import sys
input = sys.stdin.readline

n = int(input())
# test 갯수
for _ in range(n):
    m = int(input())
    operation = [input().rstrip() for _ in range(m)]
    min_heap = []
    max_heap = []
    heap_cnt = 0
    for oper in operation :
        # 문자와 숫자 split
        order, num = oper.split(' ')
        if order == "I" :
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
            heap_cnt += 1
        elif order == "D" :
            if heap_cnt > 0 :
                if num == "-1" :
                    heappop(min_heap)
                elif num == "1" :
                    heappop(max_heap)
                heap_cnt -= 1
                # 힙 카운트 0이 되면 한 번은 pop이 되었던 숫자들만 남음
                # 최대 최소 힙을 비움 list.clear()
                if heap_cnt == 0 :
                    min_heap.clear()
                    max_heap.clear()
                    
    if heap_cnt > 0 :
        print(-heappop(max_heap), heappop(min_heap))
    else :
        print("EMPTY")