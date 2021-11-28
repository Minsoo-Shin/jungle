import sys
input = sys.stdin.readline

tree = []
cnt = 0
while cnt <= 100:
    try:
        tmp = int(input().rstrip())
    except:
        break
    tree.append(tmp)
    cnt+=1

def sol(start, end):
    if start>end:
        return
    
    div = end + 1 # 초기화값

    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break
    
    sol(start + 1, div-1) # 왼쪽 서브 트리
    sol(div, end) # 오른쪽 서브트리
    print(tree[start]) # 중간 출력

