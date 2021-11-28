'''
DP로 풀 수 있는 조건인지 확인
1. 최적 조건의 해
2. 작은 문제가 중복 계산이 되고 있는지
'''
n = int(input())
d = [1000001] * (n+1) # 초기값
d[1] = 0

for i in range(2, n+1):
    d[i] = min(d[i], d[i-1] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
print(d[n])