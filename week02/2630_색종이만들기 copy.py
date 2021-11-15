import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

def g(x, y, n):
    global white, blue
    init_color = arr[x][y]  # 색종이 첫번째 원소 색깔 
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != init_color:
                g(x,y,n//2)
                g(x+n//2,y,n//2)
                g(x, y+n//2, n//2)
                g(x+n//2, y+n//2, n//2)
                return
    
    if init_color == 0:
        white += 1
    else:
        blue += 1


g(0, 0, n)
print(white)
print(blue)