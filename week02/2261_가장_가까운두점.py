import sys
INF = sys.maxsize

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# x축 기준 정렬
arr.sort()

# 두 점 사이의 거리 계산 함수
def dist(a,b):
    return (a[0] - b[0])**2 + (a[1] -b[1])**2

def closet_dist(start, end):
    # 재귀방식으로 left, right, center 삼분할로 나눈다. 
    # center의 mid 선을 중심으로 좌우 거리가 기존 저장된 것 보단 작은 점들만 계산해서 체크하면 될 것이다. 
    if start == end:
        return INF
    if end - start == 1:
        return dist(arr[start], arr[end])
    else:
        #start/end 안에 일정 거리에 있는거만 체크를 한다. 
        mid = (start + end)//2
        minDist = min(closet_dist(start, mid), closet_dist(mid, end))

        # x축 기준으로 후보 점들을 찾는다. 
        target_pl = []
        for i in range(start, end + 1):
            if (arr[mid][0] - arr[i][0])**2 < minDist:
                target_pl.append(arr[i])

        # y축 기준 정렬
        target_pl.sort(key=lambda x: x[1])

        # y축 기준으로 후보 점들 사이의 거리 비교
        t = len(target_pl)
        for i in range(t-1):
            for j in range(i+1, t):
                if (target_pl[i][1] - target_pl[j][1])**2 < minDist:
                    minDist = min(minDist, dist(target_pl[i], target_pl[j]))
                else:
                    break
        return minDist

print(closet_dist(0, n-1))