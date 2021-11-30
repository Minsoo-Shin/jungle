# 계단 오르는 속도는 한계단이나 두 계단씩 오를 수 있다. 
# 연속된 세 개의 계단은 밟을 순 없다. 
# 마지막 도착 계단은 반드시 밟아야 한다. 

# 1. 테이블 구성하기
import sys
input = sys.stdin.readline

n = int(input())
a = [0]    
for i in range(n):
    a.append(int(input()))

g = [0, 0]
h = [0, a[1]]
d = [0, 10]
for i in range(2, n+1):
    g.append(h[i-1] + a[i])
    h.append(max(g[i-2],h[i-2]) + a[i])
    d.append(max(g[i], h[i]))

print(d[n])

'''
id 0  1  2  3  4  5  6
   0 10 20 15 25 10 20
g  0  0 30 35 50 65 65
h  0 10 20 25 55 45 75
f

f(x) = max(g(x), h(x))
g(x) = h(x-1) + a(x) (idx > 2)
h(x) = max(g(x-2), h(x-2)) + a(x) (idx >= 2)
''' 