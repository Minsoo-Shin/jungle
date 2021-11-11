# 버블 정렬이란, 배열의 이웃 원소간 대소 관계를 따져서 비교, 교환하는 것인데, 
# 기존은 맨 끝(n-1)에서 맨 앞(0)까지 비교, 교환을 하고, (n-1)~(1)/(n-1)~(2) '''이렇게 반복한다. 
# 하지만, 마지막 교환 이후부턴 이미 정렬되어 있기에 비교하는건 낭비다. 
# 따라서, 마지막 원소 교환한 원소의 오른쪽 인덱스를 저장해서 range범위를 좁혀준다.  

def bubble_sort(a):
    ccnt = 0 # 비교 횟수 
    scnt = 0 # 교환 횟수
    n = len(a)
    last_pos = 0

    while last_pos < n-1:
        last = n-1
        for j in range(n-1, last_pos , -1):
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        last_pos = last

    print(f'비교는 {ccnt}, 교환은 {scnt}')

if __name__ == "__main__":
    n = int(input())
    x = [None]*n

    for i in range(n):
        x[i] = int(input('원소를 입력하시오: '))

    print("***********오름차순 정렬***********5")    
    bubble_sort(x)
    for i in range(len(x)):
        print(f'x[{i}] : {x[i]}')


