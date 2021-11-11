
'''
def check(n, array):
    maximum=max([map(max, array)])
    minimum=min([map(min, array)])
    m = n//2
    if maximum != minimum:
        return 3 #나눠야함
    else:
        return 0 #나눌필요 없음

print(check(8, arr))
'''
def cut(n)
    for r in range(n):
        for c in range(n):
            color = arr[0][0]
            if arr[r][c] == color:
                continue
            else:
                

def check(r, c, n, m) -> int: #몇번 쪼개지나
    if 
    temp = arr[r:n][c:m]
    for i in range(n-r):
        if 0 in temp and 1 in temp:
            return 0 #섞여 있다. 나눠야한다. 
        else:
            return 1 #둘다 같은게 있다


import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]    

if check(0, 0, n, n) == 1:
    result += 1
else:
    while True:
        
        