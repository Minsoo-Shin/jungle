N = int(input())
M = int(input())

need_num = [[] for _ in range(N+1)]
need_cnt = [[] for _ in range(N+1)]
ans_cnt = [0] * (N)
funda = []

for i in range(M):
    x, y, k = map(int, input().split())
    need_num[x].append(y)
    need_cnt[x].append(k)

# 기본 부품 번호
for idx, item in enumerate(need_num):
    if idx != 0 and len(item) == 0:
        funda.append(idx)

ans_cnt = [0]*(N+1)
for i in range(len(need_num[N])):
    ans_cnt[need_num[N][i]] += need_cnt[N][i]

while 1:
    sumchk = 0
    for i in funda:
        sumchk += ans_cnt[i]
    if sumchk == sum(ans_cnt):
        break

    for i in range(1, N):
        if ans_cnt[i] != 0 and i not in funda:
            for j in range(len(need_num[i])):
                ans_cnt[need_num[i][j]] += (ans_cnt[i]*need_cnt[i][j])
            ans_cnt[i] = 0

for i in funda:
    print(i, ans_cnt[i])