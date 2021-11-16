import sys
import heapq

n = int(sys.stdin.readline())
cards =[]
for _ in range(n):
    line = int(sys.stdin.readline())
    heapq.heappush(cards, line)
ans = 0
while len(cards) > 1: #카드 묶음이 한종류가 될떄까지
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    ans += (first + second)
    heapq.heappush(cards, first + second)

print(ans)
