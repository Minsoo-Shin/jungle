import sys
from itertools import permutations
from collections import deque

def calculate(operator, a, b):
        if operator == 0:
            return a + b
        elif operator == 1:
            return a - b
        elif operator == 2:
            return a * b
        else: 
            if a >= 0:
                return a // b
            else:
                return -(-a // b)
        
n = int(sys.stdin.readline())
ar = list(map(int, sys.stdin.readline().split()))
op_qty = list(map(int, sys.stdin.readline().split()))
op = []
for i in range(4):
    for _ in range(op_qty[i]):
        op.append(i)
## [0, 0, 1, 1] 

a = list(set(permutations(op)))
print(a)
max_ans = - float('inf')
min_ans = float('inf')
tmp = 0
for i in range(len(a)): # 연산자 조합마다 실행
    arr = deque(ar[:])
    for operator in a[i]: #덧셈, 뺄셈, 곱셉, 나눗셈 조합
        x = arr.popleft()
        y = arr.popleft()
        tmp = calculate(operator,x,y)
        arr.appendleft(tmp)
    max_ans = max(max_ans, tmp)
    min_ans = min(min_ans, tmp)

print(max_ans)
print(min_ans)