'''
1.아이디어
    처음 등장했다면 
        chk배열에다가 넣는다. 
    아니라면
        if 이전꺼와 같은 수인지
            pass
        else:
            if 
            set.remove(word)
        

2.시간복잡도
3.자료구조
    chk : 확인된 문자배열 []
    arr : 현재 확인할 문재 배열 []
'''

import sys
input = sys.stdin.readline 

n = int(input())
cnt = 0
for i in range(n):
    arr = list(input().strip())
    chk = set()
    lst = set(arr)

    for j in range(len(arr)):
        if arr[j] not in chk:
            chk.add(arr[j])
        else: #체크한적이 있다면
            if arr[j] == arr[j-1]:
                pass
            else:
                if arr[j] in lst:
                    lst.remove(arr[j])
    if len(set(arr)) == len(lst):
        cnt += 1
    
print(cnt)