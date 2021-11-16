from collections import deque
n, k = map(int, input().split())
ans = []
que = deque(list(range(1, n+1)))

while len(ans) < n :
    for _ in range(k):
        que.append(str(que.popleft()))
    ans.append(que.pop())

print('<%s>' % ', '.join(ans))
