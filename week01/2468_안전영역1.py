import sys

# 지역 높이/물 높이를 입력받아 안전 영역을 보여주는 행렬을 반환
def masking(heights, rain):
    mask = [[0 for i in range(n+2)] for j in range(n+2)] # 초기화 (n+2)*(n+2) 행렬 → make_graph 함수 로직 간결화를 위해서 n+2 
    for r in range(n):
        for c in range(n):
            if heights[r][c] > rain: 
                mask[r+1][c+1] = 1
    return mask

def make_graph(mask, n):
    maps = {}
    for r in range(1, n-1):
        for c in range(1, n-1):
            if mask[r][c] == 1:
                maps[(r,c)] = []
                if mask[r+1][c] == 1:
                    maps[(r,c)].append((r+1,c))
                if mask[r][c+1] == 1:
                    maps[(r,c)].append((r,c+1))
                if mask[r-1][c] == 1:
                    maps[(r,c)].append((r-1,c))
                if mask[r][c-1] == 1:
                    maps[(r,c)].append((r,c-1))
    return maps #dict
        
def DFS(graph, root):  #graph : {[0,0] : [[0,1], [1,0]]}, root : [0,0]
    visited = []  #방문했던 곳은 삭제해서 두번 안돌게
    stack = [root]  #초기 출발값

    while stack:  
        n = stack.pop()  #
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                stack += temp
    visited.sort()
    return visited

if __name__=='__main__':
    n = int(input())
    heights = [list(map(int , sys.stdin.readline().rstrip().split())) for j in range(n)]
    #[[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]  # 지역의 높이
    # 안전 영역과 잠긴 영역 구분
    max_height = max(map(max, heights))
    max_qty = []

    for rain in range(0, max_height):
        graph = make_graph(masking(heights, rain), n+2)
    ##############################################################    
        result = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i, j) in graph.keys():
                    result.append(DFS(graph, (i,j)))
            
        new_list = []
        for v in result:
            if v not in new_list:
                new_list.append(v)
        max_qty.append(len(new_list))

    print(max(max_qty))




