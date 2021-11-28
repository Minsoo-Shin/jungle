'''
1. 돌 번호가 증가하는 순서대로 점프가능
2. 첫 점프는 1, 그 뒤로 x-1, x, x+1칸 만큼 점프 가능 (단, 점프는 한 칸 이상)
3. 몇개의 돌 위에는 올라갈 수 없다. 
'''
import sys
n, m = map(int, sys.stdin.readline().split()) # n은 돌의 개수, m은 작은 돌의 갯수
sston = [int(sys.stdin.readline()) for _ in range(m)] # 작은 돌의 번호

