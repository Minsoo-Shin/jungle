# 모든 음식의 스코빌 지수를 K이상을 만드는데 걸리는 최소횟수
# 결과값 = 가장 맵지않은 스코빌지수 + 두번째로 맵지않은 스코빌지수 * 2 

'''
indexl를 힙리스트로 만든다. 
if len(indexl) == 1 and indexl[0] <k:
    return -1

최소 index를 두개를 받고 
최소값을 가진 원소가 K이상이라면, return cnt
아니라면 계산하고 append하고, cnt += 1
'''
import heapq

def solution(scoville, k):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < k: return -1
        if scoville[0] >= k: return cnt

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        result = a + b * 2
        heapq.heappush(scoville, result)
        cnt += 1
    
print(solution([7, 7], 7))