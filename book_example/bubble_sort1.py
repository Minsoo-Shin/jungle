# 버블 정렬 (bubble sort)는 이웃한 두 원소의 대소 관게를 비교하여 정렬한다.

def bubble_sort(a):
    # 버블 정렬 과정 출력

    ccnt = 0 # 비교 횟수 
    scnt = 0 # 교환 횟수
    n = len(a)

    for i in range(n-1):
        print(f'패스 { i + 1}')
        for j in range(n-1, i, -1):   #종료값은 i+1
            ###############################################
            for m in range(0, n-1):
                print(f'{a[m]:2}' + (' ' if m!= j-1 else
                                    ' +' if a[j-1] > a[j] else ' -'),
                                    end='')
                print(f'{a[n-1]:2}')
                ccnt += 1

                if a[j-1] > a[j]:
                    scnt += 1
                    a[j-i], a[j] = a[j] , a[j-i]
            
            for m in range(0, n-51):
                print(f'{a[m]:2}', end='')
            print(f'{a[n-1]:2}')
        print(f'비교를 {ccnt}번 했습니다.')
        print(f'교환을 {scnt}번 했습니다.')

if __name__ == "__main__":
    n = int(input())
    x = [None]*n

    for i in range(n):
        x[i] = int(input('원소를 입력하시오'))
    
    bubble_sort(x)

    for i in x:
        print(i)