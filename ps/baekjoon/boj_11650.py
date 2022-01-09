import sys 
input = sys.stdin.readline

n = int(input())
l = [ list(map(int, input().split())) for _ in range(n) ]
l.sort(key = lambda x: (x[0], x[1]))

for a in l:
    print(*a)



