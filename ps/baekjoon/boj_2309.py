# heights list를 받고 합을 구하고, 
# 아홉명 중에 2명의 합이 전체 합-100과 같아야함
# 찾으면 저장
# 정렬
# 차례로 출력하면서 두명과 동일하면 출력하지 않음

h = [int(input()) for _ in range(9)]
h.sort()
ssum = sum(h)
diff = ssum - 100
a, b = 0, 0    
for i in range(9):
    for j in range(i+1, 9):
        if h[i]+h[j] == diff:
            a, b = h[i], h[j]
for i in range(9):
    if h[i] not in [a, b]:
        print(h[i])