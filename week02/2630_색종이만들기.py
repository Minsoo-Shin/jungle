import sys 
N = int(sys.stdin.readline())

matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

count_one = 0
count_zero = 0

def check(start_i, start_j, n): 
    global count_one, count_zero 
    type = matrix[start_i][start_j]
    flag = True 
    
    for i in range(start_i, start_i + n):
        if not flag: 
            break 
        for j in range(start_j, start_j + n): 
            if type != matrix[i][j]: 
                flag = False 
                check(start_i, start_j, n // 2) 
                check(start_i, start_j + n // 2, n // 2) 
                check(start_i + n // 2, start_j, n // 2) 
                check(start_i + n // 2, start_j + n // 2, n // 2) 
                break
    if flag: 
        if type: 
            count_one += 1 
        else: 
            count_zero += 1 

check(0, 0, N) 
print(count_zero) 
print(count_one)