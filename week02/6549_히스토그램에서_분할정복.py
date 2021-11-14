import sys

def max_square(left, right):
    if left == right:
        return lst[left]
    else:    
        mid = (left + right) // 2
        pl = mid    # 경계선
        pr = mid + 1    # 경계선보다 한 칸 오른쪽
        min_height = min(lst[pl], lst[pr])  # 그 둘 중 작은 값
        temp = min_height * 2   # 오른쪽, 왼쪽 두 블록을 합한 넓이. 얘가 temp이다.
        # 왼쪽으로 한 칸, 오른쪽으로 한 칸씩 넓혀가면서 temp를 수정한다.
        width = 2
        while True:
            if (lst[pl] == 0 or pl == left) and (lst[pr] == 0 or pr == right):
                break # pl과 pr이 둘 다 양쪽 끝 인덱스인 left, right를 만나거나 높이가 0인 직사각형을 만나면
            # 한 쪽이 높이 0을 만나거나 끝까지 가면 다른 한 쪽만 1씩 증가시켜준다.
            elif lst[pl] == 0 or pl == left:    
                if lst[pr + 1] < min_height:    
                    min_height = lst[pr + 1]
                pr += 1
            elif lst[pr] == 0 or pr == right:
                if lst[pl - 1] < min_height:
                    min_height = lst[pl - 1]
                pl -= 1
            else: # 둘 다 갈 수 있다면 둘 다 늘려준다.
                # 둘 중 큰 높이를 골라, min_height와 비교한다. 그리고 큰 높이를 가진 쪽을 더 늘려준다.
                # 최댓값을 구해야 하기 때문
                # 큰 높이가 min_h보다 작으면 높이를 그것으로 교환한다.
                if lst[pl - 1] > lst[pr + 1]:
                    if lst[pl - 1] < min_height:
                        min_height = lst[pl - 1]
                    pl -= 1
                else:
                    if lst[pr + 1] < min_height:
                        min_height = lst[pr + 1]
                    pr += 1
            width += 1  #
            temp = max(temp, min_height * width)
        return(max(max_square(left, mid), max_square(mid + 1, right), temp))  
        # 경계선 왼쪽(max_square(left, mid))과 오른쪽(max_square(mid + 1, right)),
        # 경계선에 걸쳐 있는 최대 직사각형(temp) 중 최댓값을 반환한다.
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    n = lst[0]
    histo = lst[1:]
    if lst[0] == 0:
        break
    print(max_square(1, len(histo)))