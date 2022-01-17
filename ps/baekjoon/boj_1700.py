'''
멀티탭 스케쥴링을 해서 플러그를 뺴는 횟수를 줄이는 방법
이 후에 쓸게 많은 용품이라면?
최대한 그대로 꽂아두는게 낫다. 
1 2 3 2 3 1 1 
# 전체 리스트로 반복 사용 횟수가 적은 순으로 제거
알고리즘
[1] 0
[1, 2] 0 
[1, 3] 1
[1, 2] 2
[1, 3] 3
[1, 3] 3
[1, 3] 3

정답
[1] 0 
[1, 2] 0
[2, 3] 1
[2, 3] 0
[2, 3] 0
[3, 1] 2
[3, 1] 2

현재의 알고리즘의 문제는 당장 사용할 용품을 고려해야하지만 
한참뒤에 있는 전체적인 사용 횟수로 제거하기 때문에 문제 되는 듯 하다.
=> 어떻게 해결할까? 

- 멀티탭 구멍이 다 찰때까지는 플러그를 빼지 않는다. 
- 멀티탭 구멍이 다 찼다고 하면 플러그를 뻊는 방법이 필요하다. 
- 다음에 나올거면 굳이 뺄 필요없다. 
- 그럼 다음, 다음다음, 다다다음...어디까지 체크를 해서 해야하나..


- 이미 플러그에 있다고 하면 패스
- 아직 콘센트가 남아있다면 추가하고 패스
- 위 두가지가 아니라면 멀티에서 제거하는 기준 마련 필요
제거 기준 
1 순위 : 앞으로 사용하지 않을 용품
2 순위 : 제일 나중에 사용되는 것

'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
multi = []
cnt = 0

for i in range(k):
    if a[i] in multi: continue

    if len(multi) < n:
        multi.append(a[i])
        continue
    
    del_list = []
    flag = False
    # 멀티탭에 있는 용품 중에 앞으로 사용하지 않을 용품은 바로 뺀다. 
    for j in range(len(multi)):
        if multi[j] not in a[i:]:
            del multi[j]
            cnt += 1
            multi.append(a[i])
            flag = True
            break
        else:
            del_idx = a[i:].index(multi[j])
            del_list.append(del_idx)
    
    if flag: continue
    try :
        del multi[max(del_list)]
        multi.append(a[i])
        cnt += 1
    except:
        continue

print(cnt)

