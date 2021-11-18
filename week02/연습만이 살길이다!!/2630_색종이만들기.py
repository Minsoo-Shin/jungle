import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

def g(x, y, n):
    global white, blue
    color = arr[x][y]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != color: # 각 색종이 색깔이 맞지 않다면 4분할로 나눠서 생각하자
                g(x, y, n//2)
                g(x+n//2, y, n//2)
                g(x, y+n//2, n//2)
                g(x+n//2, y+n//2, n//2)
                return
  
    if color == 0:
        white += 1
    else:
        blue += 1

g(0,0,n)
print(white)
print(blue)