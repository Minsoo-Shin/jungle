# dp 삼각형 
#    []
# [   ,   ]

def solution(triangle):
    answer = 0
    height = len(triangle)

    dp = [[0] * i for i in range(1, height+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, height):
        for j in range(i+1):
            if j==0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j== i:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(triangle[i][j] + dp[i-1][j-1], triangle[i][j] + dp[i-1][j])
    answer = max(dp[height-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))