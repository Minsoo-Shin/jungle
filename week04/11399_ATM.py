# 사람마다 인출하는 시간이 다르다. 
# 인출하는데 기다리는 각자의 시간의 합의 최솟값을 구해라
# => 인출 시간이 낮은 순서대로 먼저하게 되면 된다.

n = int(input())
time = list(map(int, input().split()))
time.sort()

ans = 0
for i in range(1, n+1):
    sub = 0
    for j in range(i):
        sub += time[j]
    ans += sub

print(ans)