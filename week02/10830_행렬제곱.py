import sys

n, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
c = 1000

def matrixmult(A,B):
    n = len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
            C[i][j] = C[i][j] % c   
    return C

def g(a: list ,b: int):
    temp = [[0]*n for _ in range(n)]
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= c
        return a
    
    else:
        matrix =g(a, b//2)
        if b % 2 == 0:
            temp = matrixmult(matrix, matrix)
            return temp 
        else:
            temp = matrixmult(matrixmult(matrix, matrix), a)
            return temp

for ans in g(arr, b):
   print(*ans)
