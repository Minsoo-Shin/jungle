# 백준 시간초과 (내풀이)

import bisect
import sys
input = sys.stdin.readline

n = int(input())
# test 갯수
for _ in range(n):
    m = int(input())
    num = []
    operations = [input().rstrip() for _ in range(m)]
    for op in operations:
        # Insert 명령
        op = op.split()
        if op[0] == "I":
            # 아무것도 없으면 그냥 넣고
            if len(num) == 0: num.append(int(op[1]))
            else: bisect.insort(num, int(op[1])) 
        # Delete 명령
        else:
            if len(num) == 0: continue
            # 최소값 제거
            if op[1] == "-1":
                num.pop(0)
            # 최대값 제거
            else:
                num.pop()
    # 결과 반환
    if len(num) == 0: 
        print("EMPTY")
    else: 
        print(*[num[-1], num[0]])