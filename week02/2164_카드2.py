from collections import deque

arr = deque(list(range(1, int(input())+1)))

while len(arr) > 1:
    arr.popleft()
    first = arr.popleft()
    arr.append(first)

print(*arr)