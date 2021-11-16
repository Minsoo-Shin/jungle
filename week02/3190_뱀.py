import sys
from typing import Deque

n = int(input())
k = int(input())
apple = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    apple[x-1][y-1] = 1 # apple이 있다는 의미

control = [0]*10003
l = int(input())
for i in range(l):
    time, direc = input().split()
    control[int(time)] = direc

snake_dir = 'c'
dir_inform = {'a':(-1,0), 'b':(0,-1), 'c':(0,1), 'd':(1,0)}
time = 0
snake = Deque([(1,1)])

while True:
 
 
    
    head = (snake[0][0] + dir_inform[snake_dir][0], snake[0][1] + dir_inform[snake_dir][1])
    if head in snake or (head[0] < 1 or head[0] > n) or (head[1] < 1 or head[1] > n):
        break
    if apple[head[0]-1][head[1]-1] == 0: #사과가 없다면 꼬리자르기
        snake.pop()
    else:
        apple[head[0]-1][head[1]-1] = 0
    
    snake.appendleft(head)

    time += 1
    
print(time + 1)