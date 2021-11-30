# 사용횟수가 많으면 많을 수록 멀티탭에 그대로 둔다. 
# 플로그 빼는 횟수
# 빈도수 별 
import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
multi = []

for i in range(k):
    # 물품이 이미 꽂혀있으면 멀티탭이 비는지 확인할 필요가 없다. 
    # but, 멀티탭이 비는지 확인해도 물품이 이미 포함되어있는지는 확인해야하기 때문에 따로 앞으로 빼는게 유리
    if a[i] in multi: continue 

    if len(multi) < n:
        multi.append(a[i])
        continue

    del_list = []
    has_plug = True
    
    # 멀티탭에 있는 물품을 나머지 사용순서에 있는 리스트를 참조해 사용예정이라면 
    for j in range(len(multi)):
        if multi[j] in a[i:]: # 이미 multi에 없기때문에 a[i]는 미포함
            multi_index = a[i:].index(multi[j])
        else:
            multi_index = 101
            has_plug = False
        
        del_list.append(multi_index)

        if not has_plug:
            break
    
    # multi에서 뽑아할 idx를 저장
    plug_out = del_list.index(max(del_list))
    del multi[plug_out]
    multi.append(a[i])
    cnt += 1

print(cnt)


# 반례 생각하기
# 2 5
# 1 (2) (3) 2 (2) 4 1 1 1
# (1) 2 (3) 2 2 (4) 1 1 1


