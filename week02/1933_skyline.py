import sys
import heapq
N = int(sys.stdin.readline().strip())

buildings = []
for i in range(N):
    l,h,r  = map(int,sys.stdin.readline().split())
    buildings.append([l,h,r])   # 왼쪽좌표, 우측좌표, 높이 순으로 값받음.
events = sorted([(L, -H, R) for L, H, R in buildings] + list({(R, 0, None) for _, _, R in buildings}))
# 최대힙 사용할 것이기 때문에 -붙여서 sorted, 닫힌 부분을 별도로 활용할 것이기 때문에 _,R,_형태로 값받아서 리스트에] 저장.

ans = [[0, 0]] #[시작, 높이]
heap =[(0, float("inf"))] #(높이, 끝지점)
for start, Height, end in events:
        while start >= heap[0][1]: # 시작값과 heap에 저장해놓은 End값 비교
            heapq.heappop(heap) # start값보다 heap에 있는 end값이 더 작으면 pop
        if Height:  # end포인트가 아닐때(end,0,None) 형태 start 이면
            heapq.heappush(heap, (Height, end)) # 힙에 높이와 end포인트 추가
        if ans[-1][1] + heap[0][0]: # 정답에 넣어둔 높이와 heap에 넣어둔 놓이의 합이 0이 아니면 통과
            ans += [start, -heap[0][0]],    # 시작지점이랑, 높이 추가

for i in ans[1:]:
    print(*i,end=' ')