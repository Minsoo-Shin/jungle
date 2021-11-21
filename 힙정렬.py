import heapq
a = [1,100,7,4,5,25]
#/Heap을 이용한 정렬하기 (오름차순)/#
def sort(a):
    result = []
    heap = [] 
    for value in a:
        heapq.heappush(heap, value)

    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result
#/Heap을 이용한 정렬하기 (내림차순)/#
def sort_reverse(a):
    result = []
    heap = []
    for value in a:
        heapq.heappush(heap, -value)
    
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

print(sort(a))
print(sort_reverse(a))
